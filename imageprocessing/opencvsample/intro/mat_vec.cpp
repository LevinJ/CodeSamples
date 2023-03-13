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

int main(int argc, char** argv )
{
    cv::Mat m(2,3,CV_8UC3, cv::Scalar(40,80,255)); 
    float scale = 1/255.0;
    cv::Scalar mean(0.1, 0.2, 1);
    cv::Scalar variance(10, 2, 1);

    normanize(m, scale, mean, variance);  
}
