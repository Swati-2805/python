
#WAP to accept scores of two teams(say India,Pak) from user and
#make a decision which team won the match

india_score=int(input("Enter the scrore of india: "))
pakistan_score=int(input("Enter the scrore of pakistan: "))
if(india_score>pakistan_score):
    print("Team india won the match")
elif(india_score<pakistan_score):
    print("Team pak won the match")
else:
    print("The match tie")
-------------------------------------------------------------------------------
#wap to check year is leap yr or not

year=int(input("Enter the year: "))
if(year%4==0 and year%100!=0)or (year%400==0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
-------------------------------------------------------------------------------
#WAP to accept percentage from user and make a decision whether he got O grade ,
#first class,second class or failed.

percentage=float(input("Enter the percentage: "))
if(percentage>=80):
    print("O GRADE")
elif(percentage>=60):
    print("First Class")
elif(percentage>=40):
    print("Second Class")
else:
    print("Failed")
