import random
#string is a list of characters so we can loop through it
word=input("Enter a word to loop through")
for letter in word:
    print(letter)

for i in range(1,11): 
    print(i)

for i in range(9): #goes until 9
    print(i) #doesn't print a new line

for i in range(0,50,5): #increments of 5
    print(i, end=" ") #good for if you have a weird character at end and want to stop it
print("\n")
for i in range(10,0,-1):
    print(i) #10,9,8,7,6,5,4,3,2,1


message=input("enter a message")
print("\nThe length of your message is",len(message))

if "e" in message.lower():
    print("e is in your message")
else:
    print("e is not in your message")


word="index"
print(word[0]) #prints out the i
#get random letter in word
high=len(word)
low=-len(word)

for i in range(10):
    position=random.randrange(low,high)
    print("word [",position,"]\t", word[position])

#can change value of word but not string itself or create a new string

#remove vowels
message=input("Enter your message that contains vowels: ")
noVowelMessage=""
vowels="aeiou"

for letter in message:
    if letter.lower not in vowels:
        noVowelMessage+=letter
print(noVowelMessage)

word1="pizza"
print(word1[0:5])
print(word1[1:3]) #subset 
#doesnt take last item

#Tuples- can hold multiple variable types

prizeBox=()
if not prizeBox: #can treat like a condition. If there's nothing in there. 
    print(" Your prizeBox is empty")

prizeBox=("dollar bill", "pen", "fidget spinner", "sticker")

print("You have ",len(prizeBox)," prizes in your box")

if "sticker" in prizeBox:
    print("Get some better prizes")

index=int(input("Enter the number of the prize in the box"))
print("At index ",index, "is",prizeBox[index])

print("The last 2 items in the box are:",prizeBox[2:4])

#tuples are not muttable 

oldPrizeBox=("baseball cards", "breakable erasers")
prizeBox+=oldPrizeBox #recreates prize box with first things and second things

name,grade="Tehilla","B"
print("name", name)
print("grade",grade)