
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;


class string
{
    char* data;

public:

    string(const char* p)
    {
        size_t size = strlen(p) + 1;
        data = new char[size];
        memcpy(data, p, size);
    }
    ~string()
        {
            delete[] data;
        }
    string(const string& that)
       {
           size_t size = strlen(that.data) + 1;
           data = new char[size];
           memcpy(data, that.data, size);
       }
    string(string&& that)   // string&& is an rvalue reference to a string
       {
           data = that.data;
           that.data = nullptr;
       }
};

int main(){
	cout<<"hello world"<<endl;
	return 0;
}
