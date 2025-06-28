
#WAP to get factorial of a number using function
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter the number: "))
if num<0:
    print("Negative number cannot get a factorial")
else:
    print("Factorial of",num,"is",factorial(num))
-------------------------------------------------------------------------------------------------------
#WAP to find maximum among two numbers
def max_num(a,b):
    if a>b:
        return a
    else:
        return b
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
print("The maximum number among both is: ",max_num(num1,num2))
----------------------------------------------------------------------------------------------------------------
#WAP to check whether person can vote or not using function
def can_vote(age):
    if age>=18:
        return "YOU ARE ELIGIBLE TO VOTE."
    else:
        return "YOU ARE NOT ELIGIBLE TO VOTE."
age=int(input("Enter your age: "))
print(can_vote(age))
----------------------------------------------------------------------------------------------------------------------

#WAP to get table of a number using function
def cal_table(n):
    print(f"Multiplication table of {n}:")
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")
num=int(input("Enter the number: "))
cal_table(num)
