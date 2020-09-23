#include <stdio.h>

int main(void){
    float volume;
    float radius;
    printf("Enter a Shpere Radius  :  ");
    scanf("%f", &radius);
    float cubic_radius = radius * radius * radius;

    volume = 4.0f/3.0f * 22.0f/7.0f * cubic_radius;
    printf("%0.6f \n",volume);
    return volume;
}
