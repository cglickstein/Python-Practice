import os
#often csv file that can read in lines of code separated by commas or pikes like firstName, lastName, SSN
#dont need to open and close and open and close but at some point text file should be closed


current_directory = os.getcwd()

# 👇️ /home/borislav/Desktop/bobbyhadz_python
print ("******************")
print(current_directory)
print ("******************")

contents = os.listdir(current_directory)
print(contents)  


print('students.txt' in contents)  
 


#code to change current directory
dir_containing_file = r"C:\Users\rosec\OneDrive\Desktop\Documents\Python"
#change to directory containing file
os.chdir(dir_containing_file)


fileStudents=open("students.txt","r")

print(fileStudents.read(5)) #reading one character and printing that out
print(fileStudents.read(2)) #saves from pointer and continues from before


print("line 2",fileStudents.readline(2))


lines=fileStudents.readlines() #reads row by row and puts it into a list
print(lines)
print("Number of students: ",len(lines))

for line in lines: #can read all students this way. like any other list.
    print(line) 

fileStudents.close()

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
fileStudents.close()

