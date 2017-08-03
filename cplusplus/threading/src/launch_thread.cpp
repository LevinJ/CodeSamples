#include <thread>
#include <iostream>

class bar {
public:
  void foo() {
    std::cout << "hello from member function" << std::endl;
  }
  std::thread spawn() {

     return std::thread(&bar::foo, this);

   }
};

int main()
{
  bar b;
  std::thread t = b.spawn();
  t.join();
}
