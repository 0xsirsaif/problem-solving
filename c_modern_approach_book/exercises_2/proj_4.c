#include <stdio.h>

int main(void){
    float amount, tax, total;
    printf("Enter Money Amount :  ");
    scanf("%f", &amount);
    tax = 5.0/100.0 * amount;
    total = amount + tax;
    printf("Total is %.6f \n", total);
    return total;
}
