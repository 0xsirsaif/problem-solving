#include <stdio.h>

int main() {
	int enterd_num, twent_factor, tens_factor, fives_factor, ones_factor;
	
	printf("Enter Number : ");
	scanf("%d", &enterd_num);
	twent_factor = enterd_num / 20;
	tens_factor = (enterd_num % 20) / 10;
	fives_factor = ((enterd_num % 20) - tens_factor * 10) / 5;
	ones_factor = ((enterd_num % 20) - (tens_factor * 10) - (fives_factor * 5)) / 1;

	printf("20$s: %d \n10$s: %d \n5$s: %d \n1$s: %d \n",twent_factor, tens_factor, fives_factor, ones_factor );
	

	return 0;
}