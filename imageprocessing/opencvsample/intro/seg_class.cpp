#include "seg_class.hpp"
#include <filesystem>
using nvinfer1::IHostMemory;
using nvinfer1::IBuilder;
using nvinfer1::INetworkDefinition;
using nvinfer1::ICudaEngine;
using nvinfer1::IInt8Calibrator;
using nvinfer1::IBuilderConfig;
using nvinfer1::IRuntime;
using nvinfer1::IExecutionContext;
using nvinfer1::ILogger;
using nvinfer1::Dims3;
using nvinfer1::Dims2;
using Severity = nvinfer1::ILogger::Severity;
using TrtSharedEnginePtr = std::shared_ptr<ICudaEngine>;

using std::string;
using std::ios;
using std::ofstream;
using std::ifstream;
using std::vector;
using std::cout;
using std::endl;
using std::array;

using cv::Mat;


vector<vector<uint8_t>> get_color_map() {
    vector<vector<uint8_t>> color_map(256, vector<uint8_t>(3));
    std::minstd_rand rand_eng(123);
    std::uniform_int_distribution<uint8_t> u(0, 255);
    for (int i{0}; i < 256; ++i) {
        for (int j{0}; j < 3; ++j) {
            color_map[i][j] = u(rand_eng);
        }
    }
    return color_map;
}

void compile_onnx(string ep) {
    bool use_fp16{false};
    std::string engine_path = ep;
    std::string onnx_path = ep.replace(ep.end()-7, ep.end(), ".onnx");
    TrtSharedEnginePtr engine = parse_to_engine(onnx_path, use_fp16);
    // std::cout << "engine path: " << engine_path << std::endl;
    // std::cout << "onnx path: " << onnx_path << std::endl;
    serialize(engine, engine_path);
}

Segmentation::Segmentation(string ep, string md){
    engine_path = ep;
    if (!std::filesystem::exists(ep)){
        compile_onnx(ep);
    }
    engine = deserialize(engine_path);
    i_dims = static_cast<Dims3&&>(
        engine->getBindingDimensions(engine->getBindingIndex("input_image")));
    o_dims = static_cast<Dims3&&>(
        engine->getBindingDimensions(engine->getBindingIndex("preds")));
    iH = i_dims.d[2];
    iW = i_dims.d[3];
    mode = md;
    if (mode == "pred"){
        oH = o_dims.d[1];
        oW = o_dims.d[2];
    }
    else if (mode == "eval"){
        oC = o_dims.d[1];
        oH = o_dims.d[2];
        oW = o_dims.d[3];
    }
    std::cout << "input paramteters: " << iH << " , " << iW << std::endl;
    std::cout << "output parameters: " << oH << " , " << oW << std::endl;
    // oC = o_dims.d[1];
    // oH = o_dims.d[2];
    // oW = o_dims.d[3];
}

// void Segmentation::test(Mat *im){
//     std::cout << "test results: " << std::endl;
//     std::cout << im->rows << " " << im->cols << std::endl;
// }
static void hwc_to_chw(cv::InputArray src, cv::OutputArray dst) {
  std::vector<cv::Mat> channels;
  cv::split(src, channels);

  // Stretch one-channel images to vector
  for (auto &img : channels) {
    img = img.reshape(1, 1);
  }

  // Concatenate three vectors to one
  cv::hconcat( channels, dst );
}
static void normanize_img(cv::Mat &mat, float scale, cv::Scalar &mean, cv::Scalar &variance, vector<float> &array){
    cv::cvtColor(mat, mat, cv::COLOR_BGR2RGB);
    mat.convertTo(mat, CV_32FC3);
    mat *= scale;
    cv::subtract(mat, mean, mat);
    cv::divide(mat, variance, mat);
    hwc_to_chw(mat, mat);
    if (mat.isContinuous()) {
    // array.assign((float*)mat.datastart, (float*)mat.dataend); // <- has problems for sub-matrix like mat = big_mat.row(i)
    array.assign((float*)mat.data, (float*)mat.data + mat.total()*mat.channels());
    } else {
    for (int i = 0; i < mat.rows; ++i) {
        array.insert(array.end(), mat.ptr<float>(i), mat.ptr<float>(i)+mat.cols*mat.channels());
    }
    }
}
vector<int> Segmentation::infer_pred(Mat& im){
    // orgH{im.rows}; orgW{im.cols};
    orgH = im.rows;
    orgW = im.cols;
    if ((orgH != iH) || (orgW != iW)){
        cv::resize(im, im, cv::Size(iW, iH), cv::INTER_CUBIC);
    }

    // array<float, 3> mean{0.3257f, 0.3690f, 0.3223f};
    // array<float, 3> variance{0.2112f, 0.2148f, 0.2115f};
    // float scale = 1.f / 255.f;
    // for (int i{0}; i < 3; ++i){
    //     variance[i] = 1.f / variance[i];
    // }
    // vector<float> data(iH * iW * 3);
    // for (int h{0}; h < iH; ++h){
    //     cv::Vec3b *p = im.ptr<cv::Vec3b>(h);
    //     for (int w{0}; w < iW; ++w){
    //         for (int c{0}; c < 3; ++c){
    //             int idx = (2 - c) * iH * iW + h * iW + w;
    //             data[idx] = (p[w][c] * scale - mean[c]) * variance[c];
    //         }
    //     }
    // }
    
    vector<float> data;
    float scale = 1.f / 255.f;
    cv::Scalar mean2(0.3257, 0.3690, 0.3223);
    cv::Scalar variance2(0.2112, 0.2148, 0.2115);
    normanize_img(im, scale, mean2, variance2, data);

    
    auto start = std::chrono::system_clock::now();
    vector<int> res = infer_pred_with_engine(engine, data);
    auto end = std::chrono::system_clock::now();
    std::cout << "real inference time: " << std::chrono::duration<double>(end - start).count() << std::endl;

    return res;
    // return im;    
}

void Segmentation::visual_pred(Mat& im, vector<int>& res){
    // int orgH{im.rows}, orgW{im.cols};
    vector<vector<uint8_t>> color_map = get_color_map();
    int idx{0};
    for (int i{0}; i < oH; ++i){
        uint8_t *ptr = im.ptr<uint8_t>(i);
        for (int j{0}; j < oW; ++j){

            ptr[0] = color_map[res[idx]][0];
            ptr[1] = color_map[res[idx]][1];
            ptr[2] = color_map[res[idx]][2];
            ptr += 3;
            ++idx;
        }
    }
    if ((orgH != oH) || orgW != oW) {
        cv::resize(im, im, cv::Size(orgW, orgH), cv::INTER_LINEAR); 
    }
}

vector<int> Segmentation::infer_eval(Mat& im){
    // orgH{im.rows}; orgW{im.cols};
    orgH = im.rows;
    orgW = im.cols;
    if ((orgH != iH) || (orgW != iW)){
        cv::resize(im, im, cv::Size(iW, iH), cv::INTER_CUBIC);
    }
    array<float, 3> mean{0.3257f, 0.3690f, 0.3223f};
    array<float, 3> variance{0.2112f, 0.2148f, 0.2115f};
    float scale = 1.f / 255.f;
    for (int i{0}; i < 3; ++i){
        variance[i] = 1.f / variance[i];
    }
    vector<float> data(iH * iW * 3);
    for (int h{0}; h < iH; ++h){
        cv::Vec3b *p = im.ptr<cv::Vec3b>(h);
        for (int w{0}; w < iW; ++w){
            for (int c{0}; c < 3; ++c){
                int idx = (2 - c) * iH * iW + h * iW + w;
                data[idx] = (p[w][c] * scale - mean[c]) * variance[c];
            }
        }
    }
    auto start = std::chrono::system_clock::now();
    vector<int> res = infer_eval_with_engine(engine, data);
    auto end = std::chrono::system_clock::now();
    std::cout << "real inference time: " << std::chrono::duration<double>(end - start).count() << std::endl;
    return res;
    
    // return im;    
}

void Segmentation::visual_eval(Mat& im, vector<int>& res){
    vector<vector<uint8_t>> color_map = get_color_map();
    for (int i{0}; i < oH; ++i){
        uint8_t *ptr = im.ptr<uint8_t>(i);
        for (int j{0}; j < oW; ++j){
            vector<float> argmax;
            for (int k{0}; k < oC; ++k){
                argmax.push_back(res[((0 * oC + k) * oH + i) * oW + j]);
            }
            int idx = std::max_element(argmax.begin(), argmax.end()) - argmax.begin();
            
            ptr[0] = color_map[idx][0];
            ptr[1] = color_map[idx][1];
            ptr[2] = color_map[idx][2];
            ptr += 3;
        }
    }

    if ((orgH != oH) || orgW != oW) {
        cv::resize(im, im, cv::Size(orgW, orgH), cv::INTER_LINEAR); 
    }
}