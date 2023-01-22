prizeBox=["stickers","fidget spinner","fancy pens","magnet"]

print("You have", len(prizeBox),"in your prize box")

if "stickers" in prizeBox:
    print("You have really cool prizes")

print("The first item in your prizebox is: ",prizeBox[0]) #first item at 0th index

ancientPrizeBox=["cards","erasers"]
print(ancientPrizeBox)

prizeBox+=ancientPrizeBox #can add to a list

print("Now your prize box has:",prizeBox)

#tuple can't modify after you make, but list you can

prizeBox[0]="toothbrush" #can change any element

#prizeBox[6]="candy" #can't do this!

del prizeBox[0] #can delete an item in list then add something

prizeBox.append("candy")

#remove certain item
if "erasers" in prizeBox: #have to check it first because will throw error if item isn't there
    prizeBox.remove("erasers")

prizeBox.sort() #sorts in ascending order

prizeBox.sort(reverse=True) #sorts in descending order

#why ever use a tuple? Faster, sometimes have requirment 

#can have list/tuple that has list/tuple

gradebook=[("Shoshana","A"),("Penina","B"), ("Sara","A")] #list with tuples

for student in gradebook:
    print(student[0], ":", student[1])

print("The second student's name is: ", gradebook[1][0])

newStudent=("Tehilla","B")
gradebook.append(newStudent)


#if i have red hair and purse and get a new purse, changes it for all variables that point to that spot. If name variable, point to same space unless you make copy

#shared reference: they all point to the same spot in memory
chaviPurse=["Keys","wallet","purse"]
mrsMarkowitzPurse=chaviPurse
mommyPurse=chaviPurse
print("Chavi's purse has: \t\t",chaviPurse)
print("Mrs Markowitz's purse has: \t\t",mrsMarkowitzPurse)
print("Mommy's purse has: \t\t",mommyPurse)

chaviPurse.append("credit card")


mrsMarkowitzPurse=chaviPurse[:]
mommyPurse=chaviPurse[:]
print("Chavi's purse has: \t\t",chaviPurse)
print("Mrs Markowitz's purse has: \t\t",mrsMarkowitzPurse)
print("Mommy's purse has: \t\t",mommyPurse)

#Dictionary- multiple words with same meaning but have to have meaning in there

Dictionary={"key":"value"}
courseGrades ={"Chana":"A","Rina":"B","Dina":"C","Penina":"B"} #string key value pairs. 
print("Penina's grade is: ",courseGrades["Penina"])

if "Penina" in courseGradeds:
    print("Penina's grade is: ",courseGrades["Penina"])
else:
    print("Penina isn't a student in this course")

print("Avigayil's grade is: ", courseGrades.get("Avigail","N/A")
print("Meira's grade is: ", courseGrades.get("Meira"))

if student in courseGrades:
    print(student, ":", courseGrades[student])


courseGrades["Dina"]="A"
print(courseGrades)

del courseGrades["Dina"]