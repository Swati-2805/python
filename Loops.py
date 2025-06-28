#WAP to reverse a given number
def reverse_number(n):
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return rev
num=int(input("Enter the number: "))
print("Reversed number is: ",reverse_number(num))
--------------------------------------------------------------------------------------
#WAP to find factorial of a number given by user
def find_factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
num=int(input("Enter the number: "))
if num<0:
    print("Negative number are not defined for factorial")
else:
    print(f"The factorial of ",num, "is",find_factorial(num))
----------------------------------------------------------------------------------------------------------
#WAP to find table of a number(User input)using while loop
num=int(input("Enter the number: "))
i=1
print(f"Multiplication table of {num}:")
while i<=10:
    print(f"{num}*{i}={num*i}")
    i+=1
----------------------------------------------------------------------------------------------------------------------

#WAP find the largest number in a list
def largest_number(n):
    largest=n[0]
    for num in n:
        if num>largest:
            largest=num
    return largest
num_list=[20,10,4,28,23]
print("The largest number is: ",largest_number(num_list))
