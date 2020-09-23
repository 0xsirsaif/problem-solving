#include <stdio.h>
/*
print :
       *
      *
     *
*   *
 * *
  *
*/

int main(void){
    int init_tabs = 7;
    int second_tabs = 1;
    while(init_tabs >= 2){
        if(init_tabs <= 4 && init_tabs > 2){
            printf("%*c*",second_tabs,' ');
            printf("%*c*\n",init_tabs-second_tabs,' ');
            init_tabs -= 1;
            second_tabs += 1;
        }else{
            printf("%*c*\n",init_tabs+1,' ');
            init_tabs -= 1;
        }
    }
    return 0;
}

