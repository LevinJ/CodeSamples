#include "eigen3/Eigen/Dense"
#include "bar.h"
int main() {
	int size;
	for (size=1; size<9; size++) {
		vbar(size);
	}
	return 0;
}
