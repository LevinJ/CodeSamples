#include "seg_node.hpp"
// #include <filesystem>

#include <opencv2/imgproc.hpp>
#include <libipc/ipc.h>
using namespace std::chrono;

namespace enc = sensor_msgs::image_encodings;

SegmentationNode::SegmentationNode(const rclcpp::NodeOptions & node_options)
: Node("segmentation_inference_node", node_options)
{
    engine_path = declare_parameter<std::string>("engine_path", "/home/levin/workspace/ws_ros2/src/segmentation/data/20221125_vslam/model_pred.engine");
    inference_mode = declare_parameter<std::string>("mode", "pred");
    input_topic = declare_parameter<std::string>("input_topic", "/my_camera/camera_info");
    output_topic = declare_parameter<std::string>("output_topic", "segmentation/img");
    is_vis = declare_parameter<std::string>("is_vis", "True");
    result_topic = declare_parameter<std::string>("res_int_topic", "segmentation/int");

    jpg_send_ = std::make_unique<semantic_slam::JpgSend>(this, "front_view_jpg");

    // sub_image_ = image_transport::create_subscription(
    //     this, input_topic,
    //     std::bind(&SegmentationNode::colorImageCallback, this, std::placeholders::_1),
    //     "raw"
    // );
    sub_image_ = this->create_subscription<sensor_msgs::msg::CameraInfo>(input_topic, 1, std::bind(&SegmentationNode::colorImageCallback, this, _1));

    // sub_image_ = this->create_subscription<sensor_msgs::msg::CompressedImage>(
    //             input_topic, 10, std::bind(&SegmentationNode::colorImageCallback, this, _1));\

    // sub_image_ = image_transport::create_subscription(
    //     this, input_topic,
    //     std::bind(&SegmentationNode::colorImageCallback, this, _1),
    //     "raw"
    // );

    pub_image_ = image_transport::create_publisher(this, output_topic);
    pub_res_ = create_publisher<custom_interfaces::msg::SegmentationInt>(result_topic, 10);
    
    engine.reset(new Segmentation(engine_path, inference_mode));
}

void SegmentationNode::colorImageCallback(const sensor_msgs::msg::CameraInfo::SharedPtr msg)
{   
    // decode compressed images, cv::Mat img = cv_ptr->image = cv::imdecode....
    // cv_bridge::CvImagePtr cv_ptr(new cv_bridge::CvImage);
    // cv_ptr->header = ptr->header;
    // cv_ptr->image = cv::imdecode(cv::Mat(ptr->data), cv::IMREAD_COLOR);
    // cv_ptr->encoding = enc::BGR8;
    // pub_image_.publish(cv_ptr->toImageMsg());


    // auto cv_ptr = cv_bridge::toCvShare(ptr, "bgr8");
    // // cv::Mat img = img_h->image;

    // // auto img_h = cv_bridge::toCvShare(ptr, "bgr8");
    // cv::Mat img = cv_ptr->image;

    //here we actually assume the input image size is of  1920 x 1080
    static ipc::shm::handle shm_read("gscam_publisherseg",0,2);
    
    semantic_slam::TimerUtil timer;
    cv::Mat img(cv::Size(msg->width,msg->height),CV_8UC3,shm_read.get());
    img = img.clone();

    jpg_send_->pub_jpg(img, msg->header, 1.0);

    std::cout<<"send jpg="<<timer.elapsed()<<std::endl;

    img = cv::imread("/home/levin/temp/1.jpeg", cv::IMREAD_COLOR);

    // below resize is performed as camera intrinsics is based on this size
    int up_width = 1920;
    int up_height = 1080;
    if (img.cols != up_width && img.rows != up_height){
        cv::resize(img, img, cv::Size(up_width, up_height), cv::INTER_LINEAR);
    }

    


    auto start1 = high_resolution_clock::now();

    cv::Mat cameraMatrix_ = cv::Mat::eye(3, 3, CV_64F);
    cameraMatrix_.at<double>(0, 0) = 956.4780845435904;
    cameraMatrix_.at<double>(0, 2) = 942.78664049351255;
    cameraMatrix_.at<double>(1, 1) = 962.31713564916981;
    cameraMatrix_.at<double>(1, 2) = 561.56497661075241;

    cv::Mat distCoeffs_ = cv::Mat::zeros(4, 1, CV_64F);
    distCoeffs_.at<double>(0, 0) = -0.031156588740492434;
    distCoeffs_.at<double>(1, 0) = 0.0033144633153508077;
    distCoeffs_.at<double>(2, 0) = -0.010465032505083502;
    distCoeffs_.at<double>(3, 0) = 0.0039728438942010849;

    cv::Size imageSize = img.size();
    cv::Mat dst_persp = cv::Mat::zeros(imageSize, CV_8UC3);
    static cv::Mat mapx_persp = cv::Mat::zeros(img.rows, img.cols, CV_32FC1);
    static cv::Mat mapy_persp = cv::Mat::zeros(img.rows, img.cols, CV_32FC1);
    static bool first_time = true;
    static cv::Mat newIntMat_ ;
    if(first_time){
        first_time = false;
        cv::Mat newIntMat_ = cv::getOptimalNewCameraMatrix(cameraMatrix_, distCoeffs_, imageSize, 0.3, imageSize, 0, true);
    // std::cout<<"cameraMatrix_: "<<cameraMatrix_<<std::endl;
    // std::cout<<"distCoeffs_: "<<distCoeffs_<<std::endl;
    // std::cout<<"newIntMat_: "<<newIntMat_<<std::endl;
//    std::cout<<"undistored img: "<<img<<std::endl;
   
        cv::fisheye::initUndistortRectifyMap(cameraMatrix_, distCoeffs_, cv::Matx33d::eye(), newIntMat_, imageSize, CV_16SC2, mapx_persp, mapy_persp);
    }
    
    
    cv::remap(img, img, mapx_persp, mapy_persp, cv::INTER_LINEAR, cv::BORDER_CONSTANT, cv::Scalar(0,0,0) );  // correct the distortio  

    auto end2 = high_resolution_clock::now();
    auto duration2 = duration_cast<microseconds>(end2 - start1);

    std::cout << "duration2: " << duration2.count() << std::endl;


// >>> 1670413985 - 1670385185
// 28800
// >>> 28800 / 8
// 3600.0
// >>> 1670385726927374080


    int down_width = 960;
    int down_height = 544;
    // if (img.cols != down_width && img.rows != down_height){
    cv::resize(img, img, cv::Size(down_width, down_height), cv::INTER_LINEAR);
    // }
    if (inference_mode == "pred"){
        res = engine->infer_pred(img);
    }
    else if (inference_mode == "eval"){
        res = engine->infer_eval(img);
    }
    auto end3 = high_resolution_clock::now();
    auto duration3 = duration_cast<microseconds>(end3 - end2);

    std::cout << "duration3: " << duration3.count() << std::endl;

    // publish result in std::vector<int> fromat
    // in custom_interfaces/msgs/SegmentationInt.msg, with header, res, width and height
    custom_interfaces::msg::SegmentationInt int_result;
    int_result.image_header = msg->header;
    int_result.res = res;
    int_result.width = down_width;
    int_result.height = down_height;

    pub_res_->publish(int_result);
    


    if (is_vis == "True"){


        // // create a one channel null image
        // cv::Mat result_1_image(cv::Size(down_width, down_height), CV_8UC1);
        // // convert res into one channel image
        // reorg_pred(result_1_image, res);

        // // clone images for each class
        // cv::Mat image_1, image_2, image_3, image_4, image_5, image_6, image_7, image_8;
        // image_1 = result_1_image.clone();
        // image_2 = result_1_image.clone();
        // image_3 = result_1_image.clone();
        // image_4 = result_1_image.clone();
        // image_5 = result_1_image.clone();
        // image_6 = result_1_image.clone();
        // image_7 = result_1_image.clone();
        // image_8 = result_1_image.clone();

        // // find contours for each class
        // std::vector<std::vector<cv::Point>> contours_1 = find_contours_result(image_1, 1);
        // std::vector<std::vector<cv::Point>> contours_2 = find_contours_result(image_2, 2);
        // std::vector<std::vector<cv::Point>> contours_3 = find_contours_result(image_3, 3);
        // std::vector<std::vector<cv::Point>> contours_4 = find_contours_result(image_4, 4);
        // std::vector<std::vector<cv::Point>> contours_5 = find_contours_result(image_5, 5);
        // std::vector<std::vector<cv::Point>> contours_6 = find_contours_result(image_6, 6);
        // std::vector<std::vector<cv::Point>> contours_7 = find_contours_result(image_7, 7);
        // std::vector<std::vector<cv::Point>> contours_8 = find_contours_result(image_8, 8);

        // // draw contours
        // cv::Scalar colors[3];
        // colors[0] = cv::Scalar(255, 0, 0);
        // colors[1] = cv::Scalar(0, 255, 0);
        // colors[2] = cv::Scalar(0, 0, 255);
        // cv::Mat contourImage = img.clone();
        // for (size_t idx = 0; idx < contours_1.size(); idx++){
        //     cv::drawContours(contourImage, contours_1, idx, colors[idx % 3]);
        // }
        // for (size_t idx = 0; idx < contours_2.size(); idx++){
        //     cv::drawContours(contourImage, contours_2, idx, colors[idx % 3]);
        // }
        // for (size_t idx = 0; idx < contours_3.size(); idx++){
        //     cv::drawContours(contourImage, contours_3, idx, colors[idx % 3]);
        // }
        // for (size_t idx = 0; idx < contours_4.size(); idx++){
        //     cv::drawContours(contourImage, contours_4, idx, colors[idx % 3]);
        // }
        // for (size_t idx = 0; idx < contours_5.size(); idx++){
        //     cv::drawContours(contourImage, contours_5, idx, colors[idx % 3]);
        // }
        // for (size_t idx = 0; idx < contours_6.size(); idx++){
        //     cv::drawContours(contourImage, contours_6, idx, colors[idx % 3]);
        // }
        // for (size_t idx = 0; idx < contours_7.size(); idx++){
        //     cv::drawContours(contourImage, contours_7, idx, colors[idx % 3]);
        // }
        // for (size_t idx = 0; idx < contours_8.size(); idx++){
        //     cv::drawContours(contourImage, contours_8, idx, colors[idx % 3]);
        // }

        cv::Mat result_image = img.clone();
        if (inference_mode == "pred"){
            engine->visual_pred(result_image, res);
        }
        else if (inference_mode == "eval"){
            engine->visual_eval(result_image, res);
        }
        cv::imshow("res", result_image);
        cv::waitKey(0);
        pub_image_.publish(cv_bridge::CvImage(msg->header, "bgr8", result_image).toImageMsg());     
    }

    std::cout<<"process time="<<timer.elapsed()<<std::endl;


}

std::vector<std::vector<cv::Point>> find_contours_result(cv::Mat& image, int class_id){
    image.setTo(0, image < class_id);
    image.setTo(0, image > class_id);
    cv::threshold(image, image, class_id - 1, 255, cv::THRESH_BINARY);
    cv::erode(image, image, cv::Mat(), cv::Point(-1, -1), 1, 1, 1);
    cv::dilate(image, image, cv::Mat(), cv::Point(-1, -1), 1, 1, 1);
    std::vector<std::vector<cv::Point>> contours;
    cv::findContours(image, contours, cv::RETR_LIST, cv::CHAIN_APPROX_NONE);
    return contours;
}

void reorg_pred(Mat& im, vector<int>& res){
    int idx{0};
    for (int i{0}; i < im.rows; ++ i){
        uint8_t *ptr = im.ptr<uint8_t>(i);
        for (int j{0}; j < im.cols; ++j){
            ptr[j] = (uint8_t) res[idx];
            // ptr += 1;
            ++idx;
        }
    }
}


