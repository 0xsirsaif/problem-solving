#include <stdio.h>

int main(){
	int ISBN, gsi_perfix, group_identifier, publisher_code, item_number, check_digit;
	printf("Enter the ISBN grouped by - : ");
	scanf("%d-%d-%d-%d-%d", &gsi_perfix, &group_identifier, &publisher_code, &item_number, &check_digit);
	printf("GSI Perfix : %d\n", gsi_perfix);
	printf("Group Identifier : %d\n", group_identifier);
	printf("Publisher Code : %d\n", publisher_code);
	printf("Item Number : %d\n", item_number);
	printf("Check Digit : %d\n", check_digit);
	return 0;
}