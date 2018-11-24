/*
 * UtilityFunc.cpp
 *
 *  Created on: Nov 24, 2018
 *      Author: levin
 */

#include "UtilityFunc.h"

using namespace std;
using namespace cv;

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
