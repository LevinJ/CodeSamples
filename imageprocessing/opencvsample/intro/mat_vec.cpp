#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <iostream>
#include <vector>
using namespace cv;

void normanize(cv::Mat &m, float scale, cv::Scalar &mean, cv::Scalar &variance){
    m.convertTo(m, CV_32FC3);
    std::cout<<m<<std::endl<<std::endl;
    
    m *= scale;
    std::cout<<m<<std::endl<<std::endl;

    cv::subtract(m, mean, m);
    std::cout<<m<<std::endl<<std::endl;

    cv::divide(m, variance, m);
    std::cout<<m<<std::endl<<std::endl;
}

static void normanize_img(cv::Mat &mat, float scale, cv::Scalar &mean, cv::Scalar &variance, std::vector<float> &array){
    std::cout<<mat<<std::endl<<std::endl;
    mat.convertTo(mat, CV_32FC3);
    std::cout<<mat<<std::endl<<std::endl;
    mat *= scale;
    std::cout<<mat<<std::endl<<std::endl;
    cv::subtract(mat, mean, mat);
    std::cout<<mat<<std::endl<<std::endl;
    cv::divide(mat, variance, mat);
    std::cout<<mat<<std::endl<<std::endl;
    if (mat.isContinuous()) {
    // array.assign((float*)mat.datastart, (float*)mat.dataend); // <- has problems for sub-matrix like mat = big_mat.row(i)
        array.assign((float*)mat.data, (float*)mat.data + mat.total()*mat.channels());
    } else {
    for (int i = 0; i < mat.rows; ++i) {
        array.insert(array.end(), mat.ptr<float>(i), mat.ptr<float>(i)+mat.cols*mat.channels());
    }
    }

     std::cout<<mat<<std::endl<<std::endl;
}

int main(int argc, char** argv )
{
    cv::Mat mat(2,3,CV_8UC3, cv::Scalar(40,80,255)); 
    float scale = 1/10.0;
    cv::Scalar mean(0.1, 0.2, 1);
    cv::Scalar variance(10, 2, 1);

    std::vector<float> array;
    normanize_img(mat, scale, mean, variance, array);

    // normanize(m, scale, mean, variance);  
}
