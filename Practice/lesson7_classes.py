#class is a blueprint for an object. We're gonna make our own object. We define them and create instance of it and assign to variable. T
#They have their own methods (things you can do) and attributes. Methods = functions associated with that object.
#instance object = method every instance of that class method. you have to write self.

#Class: Student
#Purpose: Students in WITS

#in paranthesis is base class where gets all stuff from
class Student(object):
    
    #class attribute - created before an instantiation of the object. Related to the object itself but not an instance of the object 
    #dont need student objects to use this or class method 
    total=0


    @staticmethod #exists without creating an instance of the student. class method. refers to whole class. n/t else need to be created
    def getStudentCount():
        print("Student Count: ",Student.total)

    #means every time create object Student, has this method. cld hv other parameters after
    def printAddress(self):
        print("no known object")
    
    #means its a built in function, knows about it
    def __init__(self, firstName, lastName, street, city, state,zipcode):
        print("A new student has been created")
        #can create objects in method
        self.firstName=firstName #creating an instance of attribute and giving value of what's being passed in
        self.lastName= lastName
        self.streetAddress=street #streetAddress is attribute and street is being passed in. Attributes on the left, not right. Right is value passed in
        self.addressCity=city 
        self.addressState=state
        self.addressZipcode=zipcode 
        

    @property #needs same name as your attribute
    def gpa(self):
        return self.__gpa
    #property- method with same name as private attribute and gives read access to private attribute

    #allows you to write to gpa
    @gpa.setter
    def gpa(self,new__gpa):
        if new__gpa==" ":
            print("gpa cannot be an empty string")
        else:
            self.__gpa=new__gpa
            #can even call honor roll
            #dont need to really pass in gpa
            self.__updateHonorRoll(self.__gpa)


    def updateGPA(self, newGPA):
        if float(newGPA)<=4:
            self.__gpa=newGPA
            print("Your GPA has been updated")
            self.__updateHonorRoll(self.__gpa)
    
    #cannot access this from main because that's a dif class
    def __updateHonorRoll(self,gpa):
        if float(gpa)>=3.5:
            self.__isHonorRoll = True
            print("Honor Roll Student")
        else:
            self.__isHonorRoll = False

        #update the class attribute
        Student.total+=1

        


    #HEADERS FOR EVERY METHOD, CLASS, FILE ETC
    def printMailingAddress(self):
        print(self.streetAddress)
        print(self.addressCity,", ",self.addressState, " ",self.addressZipcode) #how to use attribute- self

        #method which returns string when try to print
    def __str__ (self):
        rep="student: \n"
        rep+="Name: "+self.firstName+" "+self.lastName+"\n"
        rep+="Address: "+self.streetAddress+" "+self.addressCity+" "+self.addressState+" "+self.addressZipcode
        return rep

    

#main

Student.getStudentCount()
witsStudent=Student("Chava","Glickstein","3011 Fallstaff Rd. Unit 201","Baltimore","MD","21209") #constructor is called automatically when a class is instantiated. define own cunstructor so more specific.
#constructor = method called when an object is instantiated. We can set up variables etc with that. You set things up. 
witsStudent2=Student("Noah","Glickstein","3011 Fallstaff Rd. Unit 201","Baltimore","MD","21209")

witsStudent.printMailingAddress() #thats how to call method on it

print(witsStudent.firstName)

print("print student.total: ", Student)

print(witsStudent)
print(witsStudent2)

Student.getStudentCount()

print("print witsStudent.total",witsStudent.total)
#attribute can be outside class method. created and exists before object instantiated. 

#everything automatically considered in python. if dont enforce how to use, someone else will come and use in the wrong way so we often use private attributes and methods

#private means only _____ can call it. private so certain activities handled in a special way
#only class can access it

witsStudent.updateGPA(2.0)

#PROPERTIES- allow you to access how object accessed or changed, sometimes impose restriction on that access. method with value you want to provide indirectly
#method allows... access to another method
#ontrol access so dont directly call. control how it's used
#MORE ON PROPERTIES AT THE TOP

print("student GPA",witsStudent.gpa)

witsStudent.gpa=" "

#OOP- taking objects and make more accessible. Objects that interact by invoking methods. Method becomes function when part of a class. 
#Let's talk more abstractly about objects. 
#Work can be managed by objects then focus on what is happening, not just how it's happening. Who needs to do what (not what being done)?
#Each object handles what's being done. 
#Objects made up of other independent objects or 
#roster has a list of students and students have courses. catalog has attributes courses = list of course objects.
#course object will figure out what's involved in a course. Objects interact with each other so still have to figure out about it.
#THE HOW IS WITHIN THE OBJECT.
#course catalog methods can be add, save etc. Within a course, you could take a test. 

#INHERITANCE- base a new class on an existing class. object is the lowest level. we can create another object and have the student inherit (gets all attributes and methods from it)
#alumni objects have degree also so dif than reg student objects