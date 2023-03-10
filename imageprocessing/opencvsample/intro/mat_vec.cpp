#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <iostream>
#include <vector>
using namespace cv;

int main(int argc, char** argv )
{
    
    cv::Mat m(2,3,CV_8UC3, cv::Scalar(40,80,255)); 
    m.convertTo(m, CV_32FC3);
    std::cout<<m<<std::endl<<std::endl;
    float scale = 1/255.0;
    
    m *= scale;
    std::cout<<m<<std::endl<<std::endl;
    // Mat dst;
    // cv::subtract(m, mean, dst);

        
    
    // std::vector<double> mean = {80, 80, 80};
    // cv::Scalar std(3,  2, 1);
    // std::cout<<m <<std::endl;
    // std::cout<<std::endl;

    cv::Scalar mean(0.1, 0.2, 1);
    cv::subtract(m, mean, m);
    // m = m.mul(Scalar(2,3,4));

    cv::Scalar variance(10, 2, 1);

    std::cout<<m<<std::endl;

}
