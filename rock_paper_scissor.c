
//Program can be improved by adding a loop and player can play it until they want to quit
#include <stdio.h>
#include <stdbool.h>
#include <time.h>
#include <stdlib.h>


int main (){
    int player_choice, comp_choice;
    

    printf("Enter Your Choice\n\t0: Rock\n\t1: Paper\n\t2: Scissor\n");
    scanf("%d", &player_choice);

    //random number generator
    srand(time(0));
    comp_choice = rand() % 3; //generates random number between 0 and 3 (including 3)

    if(player_choice == 0){
        printf("Player Chose: Rock\n");
    } else if(player_choice == 1){
        printf("Player Chose: Paper\n");
    } else if(player_choice == 2){
        printf("Player Chose: Scissor\n");
    }

    if(comp_choice == 0){
        printf("Computer Chose: Rock\n");
    } else if(player_choice == 1){
        printf("Computer Chose: Paper\n");
    } else if(comp_choice == 2) {
        printf("Computer Chose: Scissor\n");
    }

    if(player_choice == comp_choice){
        printf("DRAW\n");
        return 1;
    }

    if(player_choice == 0 && comp_choice == 2){
        printf("You Win\n");
    } else if(player_choice == 1 && comp_choice == 0){
        printf("You Win\n");
    } else if(player_choice == 2 && comp_choice == 1){
        printf("You Win\n");
    } else if(player_choice == 2 && comp_choice == 0){
        printf("You Lose\n");
    } else if(player_choice == 0 && comp_choice == 1){
        printf("You Lose\n");
    } else if(player_choice == 1 && comp_choice == 2){
        printf("You Lose\n");
    }

    return 0;
}