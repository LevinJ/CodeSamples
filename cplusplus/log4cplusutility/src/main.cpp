#include <iostream>
#include <vector>
#include "Log4cplusWrapper.h"
using namespace std;



int main(int argc, char **argv) {

	Log4cplusWrapper& ins = Log4cplusWrapper::getInstance();
	ins.test();


	return 0;
}
