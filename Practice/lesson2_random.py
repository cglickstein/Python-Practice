#import random module

# import random

# random.randint(1,6) #1,2,3,4,5,6
# random.randrange(6) #0,1,2,3,4,5

# die=random.randrange(6)+1 

# password=input("What is your password? ")
# if password =="secret":
#     print("Access granted")
# else:
#     print("You didn't get it")

# dressPrice=input("How much did you pay for the dress? ")
# if int(dressPrice)>500:
#     print("that's a lot of money. it better be for a vort")
# elif int(dressPrice)<30:
#     print("Wow. That was cheap!")
#     print("Where did you get it from? ")
# elif int(dressPrice)>100:
#     print("very nice")
#     print("Is it for weekday or shabbos? ")
# else:
#     print("your dress must be between 30 and 100")

studentCount=int(input("How many girls are in the class? "))
counter=1 #used to iterate through a list of numbers

while counter<=studentCount: #need it to be less than or equal
    studentName=input("What is the next student name? ")
    print("Hello "+studentName)
    counter+=1

#control forward slash to comment out

