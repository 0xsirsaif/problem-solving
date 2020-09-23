#include <stdio.h>

int main(){
	int first_part, second_part, third_part;
	printf("Enter phone number in [(xxx) xxx-xxx] format: ");
	scanf("(%d)%d-%d", &first_part, &second_part, &third_part);
	printf("You Entered %d.%d.%d\n", first_part,second_part,third_part);
	return 0;
}