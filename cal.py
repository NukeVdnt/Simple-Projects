import time,math
print("## CAL IS STARTING ##")
time.sleep(0.5)
print(" WLECOME TO CAL")
print(' ________    _________                                     ')
time.sleep(0.1)
print(' |           |        |    |                     ')
time.sleep(0.1)
print(' |           |________|    |                     ')
time.sleep(0.1)
print(' |           |        |    |                    ')
time.sleep(0.1)
print(' |_______    |        |    |_________            ')
time.sleep(0.1)
#name = input(" Please enter your name : ")
#print("Hello", name , "you may find the answer you are looking for" )
#select a operator
time.sleep(1)
print('             |')
time.sleep(0.1) 
print('             |')
time.sleep(0.1) 
print('             |')
time.sleep(0.1) 
print(' select a operator')
time.sleep(0.5)
operators = { 1 :'+', 2 :'-', 3 :'/', 4 :'*', 5 :'power'}
more_operators = { 6 :'factorial', 7 : 'square root', 8 :'sin()', 9 :'cos()', 10 :"tan()"}
print(operators)
print(more_operators)
time.sleep(0.5)
operator = int(input("enter your selected operator : "))
if operator == 1 :
    try:
        num1 = float(input("enter number: "))
        num2 = float(input("enter the second number: "))
        print("your answer is",num1 + num2)
    except:
        print("error")
elif operator == 2 :
    try:
        num1 = float(input("enter a number: "))
        num2 = float(input("enter second number: "))
        print("your answer is ",num1 - num2)
    except:
        print('error')
elif operator == 3:
    try:
        num1 = float(input("enter a number: "))
        num2 = float(input("enter second number: "))
        print("your answer is",num1/num2)
    except:
        print("error")
elif operator == 4:
    try:
        num1 = float(input("enter a number: "))
        num2 = float(input("enter second number:  "))
        print("your answer is ",num1*num2)
    except:
        print('error')
elif operator == 5:
    try:
        num1 = float(input("enter a number: "))
        num2 =float(input("the power upto which you want to raise a number: "))
        print("your answer is ",num1**num2)
    except:
        print('error')
elif operator == 6:
    try:
        num1 = int(input("the number whose factorial you want: "))
        print("your answer is ",math.factorial(num1))
    except:
        print("error")
elif operator == 7:
    try:
        num1 = float(input("the number whose square root you want: "))
        print("your answer is ",math.sqrt(num1))
    except:
        print('error')
elif operator == 8:
    try:
        num1 = float(input("the number whose sin value you want : "))
        print("your answer is ",math.sin())
    except:
        print('error')
elif operator == 9:
    try:
        num1 = float(input("the number whose cos value you want : "))
        print("your answer is ",math.cos())
    except:
        print("error")
elif operator == 10:
    try:
        num1 = float(input("the number whose tan ratio you want : "))
        print("your answer is ",math.tan(num1))
    except:
        print('error')
else:
    print(' INVALID OPERATOR , PLEASE HAVE A LOOK AT THE AVAILABLE FUNCTIONS')
time.sleep(0.5)    
print("|")
time.sleep(0.5) 
print("|")
time.sleep(0.5) 
print("|")
time.sleep(0.5)
print("|")
time.sleep(0.5) 
print("|")
time.sleep(0.5)
print('HOPE YOU FOUND THE ANSWER YOU WERE LOOKING FOR :))')
