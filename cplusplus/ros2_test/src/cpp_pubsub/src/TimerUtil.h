/*
 * UtilityFun.h
 *
 *  Created on: Jul 23, 2021
 *      Author: levin
 */

#ifndef VSLAM_LOCALIZATION_SEMANTIC_SLAM_LIBS_SRC_UTILITY_TIMERUTILH_
#define VSLAM_LOCALIZATION_SEMANTIC_SLAM_LIBS_SRC_UTILITY_TIMERUTILH_

#include <iostream>
#include <chrono>


namespace semantic_slam {


class TimerUtil
{
public:
	TimerUtil() : beg_(clock_::now()) {}
    void reset() { beg_ = clock_::now(); }
    double elapsed() const {
        return std::chrono::duration_cast<second_>
            (clock_::now() - beg_).count(); }

private:
    typedef std::chrono::high_resolution_clock clock_;
    typedef std::chrono::duration<double, std::ratio<1> > second_;
    std::chrono::time_point<clock_> beg_;
};

} /* namespace semantic_slam */

#endif /* VSLAM_LOCALIZATION_SEMANTIC_SLAM_LIBS_SRC_UTILITY_TIMERUTILH_ */
