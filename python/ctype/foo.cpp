#include <iostream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

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
    char *greeting = 0;
    const char* hello(char* name) {
    	char hello[] = "Hello ";
		char excla[] = "!\n";
		greeting = (char *)new char[ sizeof(char) * ( strlen(name) + strlen(hello) + strlen(excla) + 1 ) ];

		strcpy( greeting , hello);
		strcat(greeting, name);
		strcat(greeting, excla);
		return greeting;
    }
    void free_mem(){
    	delete [] greeting;
    }
}
