#include "ceres/ceres.h"
#include "glog/logging.h"
using ceres::AutoDiffCostFunction;
using ceres::CostFunction;
using ceres::Problem;
using ceres::Solve;
using ceres::Solver;
// A templated cost functor that implements the residual r = 10 -
// x. The method operator() is templated so that we can then use an
// automatic differentiation wrapper around it to generate its
// derivatives.
struct F1 {
  template <typename T>
  bool operator()(const T* const x, T* residual) const {
    residual[0] = x[0] + 10.0 * x[1];
    residual[1] = static_cast<T>(0);
    residual[2] = static_cast<T>(0);
    residual[3] = static_cast<T>(0);
    return true;
  }
};

struct F2 {
  template <typename T>
  bool operator()(const T* const x, T* residual) const {
    residual[1] = sqrt(5) * (x[2] - x[3]);
    residual[0] = static_cast<T>(0);
	residual[2] = static_cast<T>(0);
	residual[3] = static_cast<T>(0);
    return true;
  }
};

struct F3 {
  template <typename T>
  bool operator()(const T* const x, T* residual) const {
    residual[2] = (x[1] - 2.0 * x[2]) * (x[1] - 2.0 * x[2]);
    residual[1] = static_cast<T>(0);
	residual[0] =static_cast<T>(0);
	residual[3] = static_cast<T>(0);
    return true;
  }
};

struct F4 {
  template <typename T>
  bool operator()(const T* const x, T* residual) const {
    residual[3] = sqrt(10) * (x[0] -x[3]) *  (x[0] -x[3]);
    residual[1] = static_cast<T>(0);
	residual[2] = static_cast<T>(0);
	residual[0] = static_cast<T>(0);
    return true;
  }
};
int main(int argc, char** argv) {
//  google::InitGoogleLogging(argv[0]);
  // The variable to solve for with its initial value. It will be
  // mutated in place by the solver.
  double x[4] =  { 3.0, -1.0, 0.0, 1.0};
  auto &x1 = x[0];
  auto &x2 = x[1];
  auto &x3 = x[2];
  auto &x4 = x[3];
  // Build the problem.
  Problem problem;
  // Set up the only cost function (also known as residual). This uses
  // auto-differentiation to obtain the derivative (jacobian).
  CostFunction* cost_function = new AutoDiffCostFunction<F1, 4, 4>(new F1);
  problem.AddResidualBlock(cost_function, nullptr, x);

  cost_function = new AutoDiffCostFunction<F2, 4, 4>(new F2);
   problem.AddResidualBlock(cost_function, nullptr, x);

   cost_function = new AutoDiffCostFunction<F3, 4, 4>(new F3);
   problem.AddResidualBlock(cost_function, nullptr, x);


   cost_function = new AutoDiffCostFunction<F4, 4, 4>(new F4);
   problem.AddResidualBlock(cost_function, nullptr, x);

   std::cout << "Initial x1 = " << x1
                 << ", x2 = " << x2
                 << ", x3 = " << x3
                 << ", x4 = " << x4
                 << "\n";

  // Run the solver!
  Solver::Options options;
  options.minimizer_progress_to_stdout = true;
  Solver::Summary summary;
  Solve(options, &problem, &summary);
  std::cout << summary.BriefReport() << "\n";

  std::cout << "Final x1 = " << x1
              << ", x2 = " << x2
              << ", x3 = " << x3
              << ", x4 = " << x4
              << "\n";

  return 0;
}
