#class is a blueprint for an object. We're gonna make our own object. We define them and create instance of it and assign to variable. T
#They have their own methods (things you can do) and attributes. Methods = functions associated with that object.
#instance object = method every instance of that class method. you have to write self.

#class: Address -capitalized
#purpose: Address object

#classes alwayas inherit from something that has more functionality

#object is a class it's just built in. when define class, define attributes and methods of an object. 
class Address(object):
        #means its a built in function, knows about it
    def __init__(self, street, city, state,zipcode):
        print("A new student has been created")
        self.streetAddress=street #streetAddress is attribute and street is being passed in. Attributes on the left, not right. Right is value passed in
        self.addressCity=city 
        self.addressState=state
        self.addressZipcode=zipcode 

    def printMailingAddress(self): #should really be part of address 
        print(self.streetAddress)
        print(self.addressCity,", ",self.addressState, " ",self.addressZipcode) #how to use attribute- self



#class: Person
#Purpose: Person object
class Person(object):

    #student who is person who has address! Address is an attribute of a person and student is based on a person so has all attributes of person.
        #means its a built in function, knows about it
    def __init__(self, firstName, lastName, address):
        print("A new student has been created")
        #can create objects in method
        self.firstName=firstName #creating an instance of attribute and giving value of what's being passed in
        self.lastName= lastName
        self.address=address #dont have to say Address is of type Address 

    def __str__(self):
        printText=self.firstName+" "+self.lastName
        return printText





class Staff(Person):
    

    #staff person has a title so method specific for staff Person
    def SetTitle(self, newTitle):
        self.title=newTitle
    def __str__(self): #overriding print method cuz will print from here
        if (self.title=="Rabbi"):
            stringReturn=self.title+" "+self.lastName #never want rabbi with his first name
        elif (self.title!=""): #not empty
            stringReturn=self.title+" "+self.firstName+" "+self.lastName
        else:
            stringReturn=self.firstName+" "+self.LastName
        return stringReturn


#Class: Student
#Purpose: Students in WITS

#in paranthesis is base class where gets all stuff from

#now it's of person type so more features
class Student(Person):
    total=0
    #overriding the constructor from Person
    def __init__(self, firstName, lastName, address, gpa):
        
        super(Student,self).__init__(firstName, lastName,address) #calling constructor of parent class
        
        
        print("A new student has been created")
        #can create objects in method
        # self.firstName=firstName #creating an instance of attribute and giving value of what's being passed in
        # self.lastName= lastName
        # self.address=address #dont have to say Address is of type Address 
        self.updateGPA(gpa)
        Student.total+=1

    #if don't define constructor, uses Person constructor
    
    #class attribute - created before an instantiation of the object. Related to the object itself but not an instance of the object 
    #dont need student objects to use this or class method 



    @staticmethod #exists without creating an instance of the student. class method. refers to whole class. n/t else need to be created
    def getStudentCount():
        print("Student Count: ",Student.total)

    #means every time create object Student, has this method. cld hv other parameters after
    def printAddress(self):
        print("no known object")
    

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


witsStudentAddress=Address("7005 Wallis Ave","Baltimore","MD","21215")
witsStudent=Student("Meira","Markowitz",witsStudentAddress,"4.0")
witsTeacher= Staff("Benjamin","Markowitz", witsStudentAddress)
witsTeacher.SetTitle("Rabbi")
print("Student: ")
print(witsStudent)

print("Staff: ")
print(witsTeacher)


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

#POLYMORPHISM- quality of treating dif things the same and having things react in same way
#send same message to objects of dif classes and results will be dif eg str method- anything can be passed but behavior that will print object. dont need to know anything about except it will print what it should for that object. doesnt matter what object but call in same way
#treat something same way (called same way but what it does is unique to its object)
#you can treat it same way but its result is unique to its object. overriding is activity ur doing but polymorphism is concept of calling objects same way but result is unique

#creating our own module like import os. creating code that can be reused to save time and effort. logical groupings so program easier to manage and share
#module- creating file with one or more classes logically grouped together