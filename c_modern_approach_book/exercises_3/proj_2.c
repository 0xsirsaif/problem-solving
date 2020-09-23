#include <stdio.h>

int main(){
	int item_num, day, month, year;
	double price;
	printf("Enter item number :  ");
	scanf("%d", &item_num);
	printf("Enter unit price :  ");
	scanf("%lf", &price);
	if(price > 9999.99){
		printf("item must be less than 9999.99\n");
	}
	printf("Enter Date in the form [mm/dd/yy]:  ");
	scanf("%d/%d/%d", &day, &month, &year);

	printf("Item \t\t unit price \t\t purchase Date \n");
	printf("%d \t\t %f \t\t %d/%d/%d\n", item_num, price, day,month,year);
	return 0;
}