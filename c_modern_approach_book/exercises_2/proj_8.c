#include <stdio.h>

int main(){
	float loan_amount, first_amount, second_amount, third_amount, monthly_interest, interest_rate, monthly_payment;
	
	printf("Enter the Loan Amount : ");
	scanf("%f", &loan_amount);
	printf("Enter the interest rate : ");
	scanf("%f", &interest_rate);
	printf("Enter the monthly payment : ");
	scanf("%f", &monthly_payment);

	monthly_interest = ((interest_rate/100) / 12) * loan_amount;
	first_amount = (loan_amount - monthly_payment) + monthly_interest;
	second_amount = (first_amount - monthly_payment) + monthly_interest;
	third_amount = (second_amount - monthly_payment) + monthly_interest;

	printf("first: %.2f\nsecond: %.2f\nthird: %.2f\n",first_amount, second_amount, third_amount);	
	return 0;
}