#include <stdio.h>

int main(void){
    float volume;
    float radius = 10.0f;
    float cubic_radius = radius * radius * radius;

    volume = 4.0f/3.0f * 22.0f/7.0f *  cubic_radius;
    printf("%0.6f \n",volume);
    return volume;
}
