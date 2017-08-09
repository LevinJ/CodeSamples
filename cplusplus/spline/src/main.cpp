#include <cstdio>
#include <cstdlib>
#include <vector>
#include "spline.h"

int main(int argc, char** argv) {

   std::vector<double> X(7), Y(7);
   X[0]=0.1; X[1]=0.4; X[2]=1.2; X[3]=1.8; X[4]=2.0; X[5]=20; X[6]=30;
   Y[0]=0.1; Y[1]=0.7; Y[2]=0.6; Y[3]=1.1; Y[4]=0.9; Y[5]=50; Y[6]=1000;

   tk::spline s;
   s.set_points(X,Y);    // currently it is required that X is already sorted

   double x=1.5;

   printf("spline at %f is %f\n", x, s(x));

   for(int i =0; i< X.size(); i++){
	   printf("spline at %f is %f, original: %f\n", X[i], s(X[i]), Y[i]);
   }


   return EXIT_SUCCESS;
}
