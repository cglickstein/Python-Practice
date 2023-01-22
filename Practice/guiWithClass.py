from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog 

#application class which is really a frame but more than a frame because adding buttons etc
class Application(Frame):
    #master is your root
    def __init__(self,master):
        #calling the constructor for the parent
        super(Application,self).__init__(master)
        self.grid()
        self.createWidgets()
        self.buttonClicks=0

    def createWidgets(self):
        self.lblIntro=ttk.Label(self, text="Welcome to Click Counter!").grid(row=0,column=0)
        self.btnClicks = ttk.Button(self,text="click me",command=self.updateButtonLabel) #if do self its just destroying the frame and not the window
        self.btnClicks.grid()

        self.lblCourse=Label(self,text="Please enter course name")
        self.lblCourse.grid(row=0,column=0,columnspan=2,sticky='W')
        
        self.lblCourse2=Label(self,text="")
        self.lblCourse2.grid(row=1,column=0,sticky='w')
        
        self.entryCourse=Entry(self)
        self.entryCourse.grid(row=1,column=1,sticky='w')
        
        self.btnSubmit = Button(self,text="submit",command=self.getCourseDescription)
        self.btnSubmit.grid(row=2,column=0, sticky=W)

        self.txtDescription=Text(self, width=35,height=5, wrap=WORD)
        self.txtDescription.grid(row=3,column=0,columnspan=2,sticky=W)

        Label(self,text="Select all semesters that apply: ").grid(row=4,column=0,sticky=W)
        self.SemesterFall2022=BooleanVar()

        Checkbutton(self,text="Fall 2022",variable=self.SemesterFall2022, command=self.updateText).grid(row=5,column=0,sticky=W)
        
        #semester spring 2023
        self.semesterSpring2023=BooleanVar()
        Checkbutton(self,text="Spring 2023",variable=self.semesterSpring2023, command=self.updateText).grid(row=6,column=0,sticky=W)
    
        #string value to hold selection of radio button
        Label(self,text="Select required or elective: ").grid(row=7,column=0,sticky=W)
        self.courseType=StringVar()
        self.courseType.set(None) #setting to value of none- not selecting anything

        Radiobutton(self,text="Required",variable=self.courseType,value="required",command=self.updateText).grid(row=8,column=0,sticky=W)
        Radiobutton(self,text="Elective",variable=self.courseType,value="elective",command=self.updateText).grid(row=9,column=0,sticky=W)


    def getCourseDescription(self):
        courseName=self.entryCourse.get()
        if courseName !="":
            message=courseName + " is a very important course that teaches all about a very important subject"
            message+= "Your instructor will attempt to make it very interesting"
            message+="Please try not to fall asleep"
        else:
            message="Please enter course name into the entry box above"
        self.txtDescription.delete(0.0,END)  #0.0 is the row column goes until the end
        self.txtDescription.insert(0.0,message) 


    def updateText(self):
        semesters=self.entryCourse.get()+"offered \n"
        if self.SemesterFall2022.get():
            semesters+="Fall 2022 \n"
        if self.semesterSpring2023.get():
            semesters+="Spring 2023 \n"
        
        if (self.courseType.get()!="None"):
            semesters+="This course is: "+self.courseType.get()


        #just chucking it in here but might not be the best spot
        instructorName = simpledialog.askstring(title="Instructor", prompt="what's your instructors name: ")

        semesters+="Instructor name is "+instructorName+"\n"

        self.txtDescription.delete(0.0,END)
        self.txtDescription.insert(0.0,semesters)

        #showing update of checkbox and also displaying message box
        messagebox.showinfo("Course","Course Type is "+self.courseType.get())
    

        

    
    #method when click button
    def updateButtonLabel(self):
        self.buttonClicks+=1
        self.btnClicks["text"]="You have clicked this button "+str(self.buttonClicks)+" times!"


#grid manager- where things go on frame. Gride method says put it on and here's row column = where belongs. column span= span across multiple columns, sticky to justify



root = Tk() #root is the base off of what your program is. invokes the tkinter environment
#replaced when we build upon it

#create a title for the window
root.title("WITS PROGRAM")

#sizing
root.geometry("300x200")

app=Application(root)




root.mainloop()

