#include <iostream>
#include <eigen3/Eigen/Dense>
 
int main()
{
  Eigen::VectorXd v(7);
  v<<0, 1, 2, 3, 4, 5, 6;
  std::cout<<v<<std::endl;
  std::cout<<v(0)<<std::endl;

  auto pose = v.tail(6);
  std::cout<<"pose: " <<pose<<std::endl;
}