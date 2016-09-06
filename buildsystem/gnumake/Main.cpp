// hello.cpp
//https://www3.ntu.edu.sg/home/ehchua/programming/cpp/gcc_make.html
#include <iostream>
using namespace std;

#include "Test1.h"
#include "Test2.h"
int main() {
   cout << "Hello, world! from main" << endl;
   test1();
   test2();
   return 0;
}
