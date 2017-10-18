#include <iostream>
#include <chrono>
#include<vector>
using namespace std;




int main()
{
	auto accumulate_func = [](int accumulator, int i){
	   return accumulator + i;
	 };
	vector<>
	int res = accumulate_func(1,1);
	cout << res<<endl;
	return 0;
}
