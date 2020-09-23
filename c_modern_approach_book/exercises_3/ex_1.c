#include <stdio.h>

 int main(){
 	printf("%6d,%4d\n", 86,1040); // >>[four spaces]86,1040
 	printf("%12.5e\n", 30.253); //>>[one space][the number before the point][.][five numbers without e][e and the exponent]
 	printf("%.4f\n", 83.162); // add [0] at the end of the number
 	printf("%-6.2g\n", .0000009979);
 	return 0;
 }