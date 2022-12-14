#include <stdio.h>

int pregunta(int edad) {
	int input;
	printf("edad?\n");
	
	sscanf("%d", input);
	printf("tengo ");
	puts(input);
	printf(" años\n");
	return 0;
}		
int main(void) {
	int edad;
	pregunta(edad);
  return 0;	
	



}
