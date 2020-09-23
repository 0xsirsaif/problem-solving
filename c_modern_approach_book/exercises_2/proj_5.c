#include <stdio.h>

int main(void){
    float x,total;
    printf("Enter X Value :  ");
    scanf("%f", &x);
    total = 3.0f * x*x*x*x*x + 2.0f * x*x*x*x - 5.0f * x*x*x - x*x + 7.0f * x - 6;
    printf("Total is %.7f \n", total);
    return total;
}
