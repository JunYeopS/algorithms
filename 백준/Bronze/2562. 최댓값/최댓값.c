#include <stdio.h>

int main(void){ 
    int nums[9]; 
    int best_value = 0;
    int best_value_index =0;

    for (int i = 0; i<9; i++){
        scanf("%d", &nums[i]);
    };
    for (int j = 0; j<9; j++){
        int num = nums[j];
        if (num > best_value){
            best_value = num;
            best_value_index =j;    
        };
    };
    printf("%d\n%d\n",best_value,best_value_index+1);
}