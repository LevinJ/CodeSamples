#include <iostream>
#include <vector>
class A
{
public:
  A (int x_arg) : x (x_arg) { std::cout << "A (x_arg)\n"; }
  A () { x = 0; std::cout << "A ()\n"; }
  A (const A &rhs) noexcept { x = rhs.x; std::cout << "A (A &)\n"; }
  A (A &&rhs) noexcept { x = rhs.x; std::cout << "A (A &&)\n"; }

private:
  int x;
};

int main ()
{
  {
    std::vector<A> a;
    std::cout << "call emplace_back:\n";
    a.emplace_back (0);
  }
  {
    std::vector<A> a;
    std::cout << "call push_back:\n";
    a.push_back (1);
  }
  return 0;
}