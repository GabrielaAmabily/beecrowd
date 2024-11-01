#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    int nivea = 0;
    char s[4];

    scanf("%s", s);

    for(int i = 0; i < 4; i++){
        if(s[i] == '+'){
            nivea++;
        }
        else if(s[i] == '-'){
            nivea--;
        }
    }
    printf("%d", nivea);
}



