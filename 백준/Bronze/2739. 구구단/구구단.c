#include <stdio.h>

int main(void) {
    int n_table;

    scanf("%d", &n_table );

    for (int i = 1; i<=9; i++){
        printf("%d * %d = %d\n",n_table,i, n_table*i );
    }
    return 0;
}
