#include <stdio.h>
#include <stdlib.h>
int main(){
    char card_name[3];
    int val=0;
    int count=0;
    while(card_name[0]!='X'){
        puts ("Enter the card_name: ");
        scanf("%2s", card_name);
    
        switch(card_name[0]){
            case 'K':
                val=10;
                break;
            case 'Q':
                val=10;
                break;
            case 'J':
                val=10;
                break;
            case 'A':
                val=11;
                break;
            case 'X':
                puts("Game ended");
                continue;
            default:
                val=atoi(card_name);
                if (val>10 || val<1){
                    puts("Invalid Card Number ,please enter a number between 1 and 10");
                    continue;
                }        
            }
        
        /*Check if the card value is between 3 and 6 inclusive then raise count*/
        if(val<=6 && val>=3){
            count++;
            puts("Count has gone up");
        }
        /*Check if the card value is 10 ,in other words 10 or jack or king or queen then lower count*/
        else if (val==10){
            count--;
            puts("Count has gone down");
        }
        printf("The current count is : %i\n",count);
    }
    return 0;

} 