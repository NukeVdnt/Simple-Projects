
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>

int main (){
    
    int number_chosen, try_counter = 1, guess;

    //Random number generator
    srand(time(0));
    number_chosen = rand() % 100+1; //genrates random number between 1 & 100
    // printf("The chosen number is %d\n", number_chosen);

    do {
        printf("Guess the number between 1 to 100\n");
        scanf("%d", &guess);
        if(number_chosen > guess){
            printf("Try for a greater number\n");
        } else if (number_chosen < guess) {
            printf("Try for a smaller number\n");
        } else {
            printf("You Win! you guessd the number in %d attempt(s)\n", try_counter);
        }
        try_counter++;
    } while(number_chosen != guess);

    return 0;
}