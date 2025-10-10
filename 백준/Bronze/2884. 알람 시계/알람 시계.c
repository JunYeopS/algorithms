#include <stdio.h>

int main(void) {
    int h, m;
    scanf("%d %d", &h, &m);
    if (m < 45) {
        m = m + 60 - 45;     
        if (h == 0){
            h = 23;
        }else{
            h -=1;
        }
    } else {
        m -= 45;
    }
    printf("%d %d\n", h, m);
    return 0;
}