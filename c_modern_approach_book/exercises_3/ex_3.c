#include <stdio.h>

int main(){
	// scanf("%d") == scanf("% d")
	int x,y,a,b,c,d,z;
	// scanf("%d-%d-%d") == scanf(%d- %d- %d)
	// scanf("%d", &x);
	// scanf(" %d", &y);
	// printf("%d\n", x);
	// hello world
	// printf("%d\n", y);

	scanf("%d-%d-%d", &x,&y,&z);
	printf("%d %d %d\n", x,y,z);
	printf("\n");
	scanf("%d- %d- %d", &b,&c,&d);
	printf("%d %d %d\n", b,c,d);
	//scanf("%f") == scanf("%f ")
	// sanf("%f,%f") != 
	return 0;
}
