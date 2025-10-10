#include <stdio.h>

int sum(int, int);

int main(void){
    int a ,b; 
    scanf("%d %d",&a, &b);
    printf("%d\n",sum(a,b));
}

int sum(int num1,int num2){
    return num1 + num2;
}