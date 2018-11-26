/*
 * UtilityFunc.cpp
 *
 *  Created on: Nov 24, 2018
 *      Author: levin
 */

#include "UtilityFunc.h"
#include <Eigen/Core>
#include <Eigen/Geometry>
#include <opencv2/core/eigen.hpp>
#include <cmath>

using namespace std;
using namespace cv;
using namespace Eigen;

string repre_mat(Mat mat){
	const int type = mat.type();
	stringstream res;
	res<<"[";
	for(int row = 0; row < mat.rows; ++row) {
		res<<"[";
		for(int col = 0; col < mat.cols; ++col) {

			if(CV_32F == type){
				res<<mat.at<float>(row, col);
			}else if(CV_64F == type){
				res<<mat.at<double>(row, col);
			}else if(CV_8U == type){
				res<<mat.at<char>(row, col);
			}
			if(col != mat.cols-1){
				res <<",";
			}

		}
		res<<"]";
	}
	res<<"]";

	return res.str();
}

std::string repre_euler(cv::Mat mat){
	Eigen::Matrix<float,3,3> eigenT;
	cv2eigen(mat,eigenT);

	stringstream ss;
	ss<<"[";
	Eigen::Vector3f euler_angles =eigenT.eulerAngles ( 2,1,0 );
	for (size_t i = 0, nRows = euler_angles.rows(), nCols = euler_angles.cols(); i < nRows; ++i){
		for (size_t j = 0;  j < nCols; ++j){
			euler_angles(i,j) = euler_angles(i,j) * 180.0/M_PI;
			ss<<euler_angles(i,j);
		}
		if(i != nRows-1){
			ss<<",";
		}
	}

	ss<<"]";
	return ss.str();
}
