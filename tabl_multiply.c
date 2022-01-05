#include<stdio.h>
#include<stdlib.h>
int main(){
    int input, i;
    printf("input namber fix: ");
    scanf("%d", &input);
    for ( i = 0; i < input; i++)
    {
        /* code */
        printf("%d x %d = %d\n",input, i, i*input);

    }
    
}