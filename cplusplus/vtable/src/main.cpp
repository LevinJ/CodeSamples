
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;


class Base {
    public:
        virtual ~Base() { }
        virtual void method() = 0;
};

class Derived: public Base{
    public:
        virtual ~Derived() {}
        void method() {}
};

int main() {
    Base* m = new Derived();
    delete m;
}
