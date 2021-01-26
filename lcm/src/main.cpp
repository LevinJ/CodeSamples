#include <iostream>
#include <lcm/lcm-cpp.hpp>
#include "exlcm/HEADER.hpp"
#include "exlcm/Image.hpp"
#include "exlcm/Imu.hpp"

using namespace std;
class Handler
{
    public:
        ~Handler() {}
        void handleMessage(const lcm::ReceiveBuffer* rbuf,
                const std::string& chan,
                const exlcm::Imu* msg)
        {
        	auto &imu_data = *msg;
        	cout<<"time="<<imu_data.header.nTimeStamp<<", count ="<<imu_data.header.nCounter<<endl;
        }
};
int main(int argc, char** argv)
{
    lcm::LCM lcm;
    if(!lcm.good())
        return 1;
    Handler handlerObject;
    lcm.subscribe("imu", &Handler::handleMessage, &handlerObject);
    while(0 == lcm.handle());
    return 0;
}
