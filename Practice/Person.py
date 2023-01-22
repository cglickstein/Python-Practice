#Person module!!!!!!!
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

if __name__=="__main__":
    print("this is a module meant to be imported (can't just run Person module- it won't do anything. these just class definitions.")