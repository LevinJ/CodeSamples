#include <iostream>
#include <lcm/lcm-cpp.hpp>
#include "exlcm/HEADER.hpp"
#include "exlcm/Image.hpp"
#include "exlcm/Imu.hpp"
#include <ctime>

#include <chrono>
#include <thread>

using namespace std;
int main(int argc, char ** argv)
{
    lcm::LCM lcm("udpm://239.255.76.67:7667?ttl=1");
    if(!lcm.good())
        return 1;
    static int imu_cnt = 0;
    while(true){
    	exlcm::Imu imu_data;
    	imu_data.header.nCounter = imu_cnt++;
    	imu_data.header.nTimeStamp = std::time(nullptr);
    	lcm.publish("imu", &imu_data);
    	cout<<"time="<<imu_data.header.nTimeStamp<<", count ="<<imu_data.header.nCounter<<endl;
    	std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }

    return 0;
}
