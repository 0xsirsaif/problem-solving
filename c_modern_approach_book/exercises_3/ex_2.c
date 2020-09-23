#include <stdio.h>

int main(){
	// Exponential notion: left-justified in a field of size 8:one digit after the decimal point.
	double x = 123456789.963258741;

	printf("%-8.1e\n", x);
	printf("%10e\n", x);
	printf("\n");
	printf("%f\n", x);
	printf("\n");
	printf("%-8.3f\n", x);
	printf("%6.0f\n", x);
	return 0;
}