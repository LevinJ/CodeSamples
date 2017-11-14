#include <iostream>
#include <string>

using namespace std;

class Foo{
    public:
        void bar(){
            std::cout << "Hello world" << std::endl;
        }
        void bar_2(const char *pstr){
        	std::cout << string(pstr) << std::endl;
        }

        void bar_3(int i){
               	std::cout <<"this is it, "<< i << std::endl;
               }
};

extern "C" {
    Foo* Foo_new(){ return new Foo(); }
    void Foo_bar(Foo* foo){ foo->bar(); }

    void Foo_bar_2(Foo* foo, const char *pstr){foo->bar_2(pstr);}

    void Foo_bar_3(Foo* foo, int i){foo->bar_3(i);}
}
