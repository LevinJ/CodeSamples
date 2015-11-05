 #include <stdlib.h>
#include <stdio.h>

  void f(void)
  {
     int* x = (int *)malloc(10 * sizeof(int));
     x[10] = 0;        // problem 1: heap block overrun
  }                    // problem 2: memory leak -- x not freed

  int main(void)
  {
    printf("Here we start the call...\n");
    f();
    printf("Here we end the call22...\n");
    return 0;
  }