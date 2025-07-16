#include<stdio.h>

int main(){
    int a00 = 1;
    int a01 = 2;
    int a10 = 3;
    int a11 = 4;
    int b00 = 5;
    int b01 = 6;
    int b10 = 7;
    int b11 = 8;

    int c00 = a00*b00 + a01*b10;
    int c01 = a00*b01 + a01*b11;
    int c10 = a10*b00 + a11*b10;
    int c11 = a10*b01 + a11*b11;

    printf("%d %d\n", c00, c01);
    printf("%d %d\n", c10, c11); 
}