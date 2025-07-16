#include<stdio.h>

int main() {
    int n = 10;
    int a0 = 0;
    int a1 = 1;
    int fib;
    for (int i = 2; i<=n; i++) {
        fib = a0+a1;
        a0 = a1;
        a1 = fib;
    }
    printf("%d\n", fib);
}