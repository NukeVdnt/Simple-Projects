#include <iostream>
#include <string>
#include<cmath>
#include<unistd.h>
int factorial();
double percent();
int main(){    
    std::string name;
    sleep(1);

    std::cout << "CAL IS STARTING " << std::endl;
    std::cout << " ______    ______         "<< std::endl;
    std::cout <<" |         |      |   |    "<< std::endl;
    std::cout <<" |         |______|   |      "<< std::endl;
    std::cout <<" |______   |      |   |_______ "<< std::endl;
    std::cout << "please enter your name: " << std::endl;
    std::cin >> name;
    sleep(0.5);
    std::cout << "Hello, "<< name <<" hope you may find the answer you are looking for " << std::endl;
    std::cout <<"LOADING OPERATORS "<< std::endl;
    sleep(0.5);
    std::cout <<"|"<< std::endl;
    sleep(0.5);
    std::cout <<"|"<< std::endl;
    sleep(0.5);
    std::cout <<"|"<< std::endl;
    sleep(0.25);
    std::cout << " 1 : + , 2 : - , 3 : / , 4 : * , 5 : power \n 6 : square root , 7 : factorial , \n 8 : sin() , 9 : cos() , 10 : tan()\n, 11 : percent(%)\n";
    
    
    int op ;
    std::cout << "enter a opertator: \n";
    std::cin >> op;  
    if(op == 1){
        double num1 , num2 ;
        std::cout << "enter a number: \n";
        std::cin >> num1;
        std::cout << "enter another number: \n";
        std::cin >> num2;
        std::cout << "the answer is " <<num1 + num2 << "\n";
    } else if(op == 2) {
        double num1 , num2;
        std::cout << "enter a number: \n";
        std::cin >> num1;
        std::cout << "enter another number: \n";
        std::cin >> num2;
        std::cout << "the answer is " <<num1 - num2 << "\n";
    } else if(op == 3){
        double num1 , num2;
        std::cout << "enter a number: \n";
        std::cin >> num1;
        std::cout << "enter another number: \n";
        std::cin >> num2;
        std::cout << "the answer is " <<num1 / num2 << "\n";
    } else if(op == 4){
        double num1 , num2;
        std::cout << "enter a number: \n";
        std::cin >> num1;
        std::cout << "enter another number: \n";
        std::cin >> num2;
        std::cout << "the answer is " <<num1 * num2 << "\n";
    } else if(op == 5){
        double num1;
        int num2;
        std::cout << "enter a number: \n";
        std::cin >> num1;
        std::cout << "enter the power you want to raise the number to: \n";
        std::cin >> num2;
        std::cout << "the answer is " << pow(num1 , num2) << "\n";       
    } else if(op == 6){
        double num1;
        std::cout << "the number whose square root you want: \n";
        std::cin >> num1;
        std::cout << "the answer is " << sqrt(num1) << "\n";   
    } else if(op == 7){
        factorial();
    } else if(op == 8){
        double angleDegree , result ;
        std::cout << "enter the angle in DEGREES: \n";
        std::cin >> angleDegree;
        result = angleDegree * (3.14 / 180);
        std::cout << "the answer is " << sin(result) << "\n";
    } else if(op == 9) {
        double angleDegree , result ;
        std::cout << "enter the angle in DEGREES: \n";
        std::cin >> angleDegree;
        result = angleDegree * (3.14 / 180);
        std::cout << "the answer is " << cos(result) << "\n";
    } else if (op == 10){
        double angleDegree , result ;
        std::cout << "enter the angle in DEGREES: \n";
        std::cin >> angleDegree;
        result = angleDegree * (3.14 / 180);
        std::cout << "the answer is " << tan(result) << "\n";
    } else if (op==11){
        percent();
    } else {
        std::cout << "INVALID OPERATOR , please check the available operators again \n";
    }
    sleep(0.5);
    std::cout <<"|"<< std::endl;
    sleep(0.5);
    std::cout <<"|"<< std::endl;
    sleep(0.5);
    std::cout <<"|"<< std::endl;
    sleep(0.5);
    std::cout <<"hope you found the answer you were looking for :))"<< std::endl;
    return 0;
}
int factorial(){
    int num , result = 1 ;
    std::cout << "the number whose factorial you want: \n";
    std::cin >> num;
    if(num > 0){
          for(int i = 1; i <= num ; i++){
          result *= i;   
        } std::cout << "the factorial of "<< num << " is " <<  result << std::endl;
    } else if(num == 0){
         std::cout << "the factorial of 0 is 1 \n";
    } else {
         std::cout << "the factorial of negative number does not exist \n ";
    }  
} 
double percent(){
   double obtainedResult,total,finalResult;
   std::cout<<"the sum of the numbers: "<<"\n";
   std::cin>>obtainedResult;
   std::cout<<"the total: "<<"\n";
   std::cin>>total;
   finalResult=(obtainedResult/total)*100;
   std::cout<<finalResult<<"%"<<std::endl;
}    
