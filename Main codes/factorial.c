#include<stdio.h>

int main() {
    int n = 6;
    int fact = 1;
    while (n > 0) {
        fact *= n;
        n--;
    }
    printf("%d\n", fact);
}