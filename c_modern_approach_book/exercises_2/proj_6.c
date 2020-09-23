#include <stdio.h>

int main(void){
    float x,total;
    printf("Enter X Value :  ");
    scanf("%f", &x);
    total = ((((3.0f * x + 2)*x - 5)*x - 1)*x + 7)*x - 6;
    printf("Total is %.7f \n", total);
    return total;
}
