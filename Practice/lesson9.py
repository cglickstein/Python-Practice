
#explain module
import Person #module name is module name.py and when import give module name
witsStudentAddress=Person.Address("7005 Wallis Ave","Baltimore","MD","21215") #need to put Person because how else would know which address?
witsStudent=Person.Student("Meira","Markowitz",witsStudentAddress,"4.0")
witsTeacher= Person.Staff("Benjamin","Markowitz", witsStudentAddress)
witsTeacher.SetTitle("Rabbi")
print("Student: ")
print(witsStudent)

print("Staff: ")
print(witsTeacher)

# roster is your master list of students. course, student, roster
# making these into classes

#roster 

#objects can contain and interact with other objects
#4 files