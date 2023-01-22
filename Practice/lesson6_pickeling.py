import os
import pickle
#pickeling-you preserve complex data in or original forml like a list or dict. pickle lets storea and shelf lets you access pickled items

#code to change current directory
dir_containing_file = r"C:\Users\rosec\OneDrive\Desktop\Documents\Python"
#change to directory containing file
os.chdir(dir_containing_file)


fileStudents=open("students.txt","r")

print(fileStudents.read(5)) #reading one character and printing that out
print(fileStudents.read(2)) #saves from pointer and continues from before


print(fileStudents.readline())
print(fileStudents.readline())

lines=fileStudents.readlines() #reads row by row and puts it into a list
print(lines)
print("Number of students: ",len(lines))

for line in lines: #can read all students this way. like any other list.
    print(line) 

fileStudents=open("students2.txt","w")
fileStudents.write("Chaya\n")
fileStudents.write("Shalava\n")
fileStudents.write("Temima\nShifra\nChava\n")
fileStudents.close()
fileStudents.close()

fileStudentsOrig=open("students.txt","r")
studentList=fileStudentsOrig.readlines()
studentList+=["Batsheva"]
print("Student List: ")
print(studentList)
fileStudents=open("newStudentList.txt","w")
fileStudents.writelines(studentList)


courseList=["ACCT100","CIS204","MATH400"]

gradeList= ["A","B","C","D","E"]

fileSchool=open("school.dat","wb") #writebinary

pickle.dump(studentList,fileSchool) #wouldn't know what's a list in text file. saves it as list or any else in original form
pickle.dump(courseList,fileSchool)
pickle.dump(gradeList,fileSchool)
fileSchool.close()

fileSchool = open("school.dat","rb") #readbinary

studentListRead = pickle.load(fileSchool)
courseListRead=pickle.load(fileSchool)
gradeListRead=pickle.load(fileSchool)

#pulls out each thing and uses it as it used it before
print("Student List: ",studentList)
print("CourseList: ",courseList)
print("Grade List: ",gradeListRead)

