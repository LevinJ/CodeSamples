#include <iostream>
#include <eigen3/Eigen/Dense>

int main()
{
  // Eigen::VectorXd v(7);
  // v<<0, 1, 2, 3, 4, 5, 6;
  // std::cout<<v<<std::endl;
  // std::cout<<v(0)<<std::endl;

  // auto pose = v.tail(6);
  // std::cout<<"pose: " <<pose<<std::endl;

  Eigen::MatrixXd mat(2, 4);
  mat << 1, 2, 6, 9,
      3, 1, 7, 2;

      Eigen::MatrixXd mat2 = mat.colwise().mean();
      std::cout<<"mean; "<<mat2<<std::endl;

      // mat = mat.colwise().mean();
      // std::cout<<"mean; "<<mat<<std::endl;

  std::cout << "Column's maximum: " << std::endl
            << mat.colwise().mean() << std::endl;
}