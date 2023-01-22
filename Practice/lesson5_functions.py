#NEED HEADERS
#Function Name: Instruction
#Purpose: gives instructions to the user
#Parameters: none
#Return value: none 
#Developer Notes: (as developer I decided to do this b/c of that or explained in this article...) u don't have to put in if none

def instructions():
    print("Welcome to my program")
    print("Press 1 for customer service")

#Function: getName
#Purpose: Gets the name from the user input
#Parameters: none
#Return value: name-string
def getName():
    name = input("What is the name of the student?")
    return name

#Function: getInput
#Purpose: Gets the input from the user
#Parameters: question-string
#Return value: name-string
"""getInput-gets name of user""" #when you hover over function in main, shows this 
def getInput(question):
    inputValue=input(question)
    return inputValue

#Function: printCourseGrade
#Purpose: print course name and grade
#Parameters: course-string
#              grade-course 
#return value: none

#can set default parameter so grade="A" here so that if don't give a course, it automatically gives an A but then every parameter after that in function needs default 
def printCourseGrade(course,grade):
    print("Course: ", course, "Grade: ",grade)

#Function addStudent
#Purpose: Add student to the class list
#Parameter: studentName
#Return value:none
def addStudent(studentName):
    global classList #can change it
    classList.append(studentName)

def main():
    addStudent("Shoshana")
    print(classList)


#main. call function.
#when debug, step into to go into method
#parameters- take value to be used in function, returns anything you'll need later on in the program
# instructions()
# # studentName=getName()
# # print(studentName)
# courseName=getInput("What is the course name?")
# grade=getInput("What is the grade? ")
# print("course ", courseName)
# print("grade ",grade)
# course="ACTT100"
# grade="A"
# printCourseGrade(course,grade)
# printCourseGrade(grade="CIS100", course="A")
# print("The end")


#Global Scopes
#var created in global scope- global var
#var created in function-local var
#global list because grades don't change 

#in global scope so global
classList=[]
main()