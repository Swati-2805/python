
#WAP to find greatest among two numbers

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
if(num1>num2):
    print(f"{num1}is a greater number")
elif(num2>num1):
    print(f"{num2}is a greater number")
else:
    print("Both are equal")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#WAP to find whether person is eligible to vote or not.

age=int(input("Enter the age: "))
if(age>=18):
    print("The person is eligible to vote")
else:
    print("The person is not eligible to vote")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#WAP to check whether the number is even or not.
number=int(input("Enter the number: "))
if(number%2==0):
    print("The given number is even")
else:
    print("The given number is odd")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#WAP to accept basic salary from user and Give 10% of DA on basic salary ,12% HRA on basic salary  to employee if the salary is more than 50000 .calculate total salary.
basic_salary=int(input("Enter the basic salary: "))
if(basic_salary>50000):
    da=0.10*basic_salary
    hra=0.12*basic_salary
    total_salary=basic_salary+da+hra
    print(f"DA={da}")
    print(f"HRA={hra}")
    print(f"TOTAL SALARY={total_salary}")
else:
    print(f"TOTAL SALARY(NO DA AND HRA APPLIED)={basic_salary}")
