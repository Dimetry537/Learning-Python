#include <stdio.h>

int main() {
    int x = 10;
    do {
        x -= 1;
        printf("%d", x);
    } while(x > 0);
}