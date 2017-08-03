#include <iostream>
#include <chrono>
#include <vector>
#include <cmath>


using namespace std;


double logistic(double x){

	return 2.0 / (1 + exp(-x)) - 1.0;

}

double lane_speed_cost(double target_lane_speed){

	return logistic(22/target_lane_speed);
}

int main()
{
	vector<double> speeds = {1000, 20.7836, 0};
	for(auto &speed: speeds){
		cout << "speed="<<speed<<"logistic="<<lane_speed_cost(speed)<<endl;
	}

	return 0;
}
