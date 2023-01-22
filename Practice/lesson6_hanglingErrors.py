#handling errors gracefully with try catch statements

try:
    num=float(input("Enter a number: "))
except:
    print("something went wrong")

try:
    num=float(input("Enter a number: "))
except ValueError as e: #more specific, if wrong value
    print("this is not a number")
    print(e) #e is variable that holds error message. many things you can access from the error
else: #runs if the try is successful 
    print("Good value") 

#force error to see what kind of error is happening

gradeList=[100,95,"B",None] #none is null

for grade in gradeList:
    try:
        print("Converting grade to percent ",grade)
        print(float(grade),"%")
    except(TypeError, ValueError):
        print("invalid grade!!!!")

for grade in gradeList:
    try:
        print("Converting grade to percent ",grade)
        print(float(grade),"%")
    except(TypeError):
        print("can only convert a string or a number")
    except(ValueError):
        print("can only convert a string of digits")

