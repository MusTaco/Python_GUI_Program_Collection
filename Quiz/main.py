#libraries/frameworks used
from tkinter import *
from tkinter import messagebox
import os

#Questions to appear
thefile = open('questions.txt', 'r')
Questions = {}
for line in thefile:
    x=line.split(',')
    a=x[0]
    b=x[1].strip()
    Questions[a]=b




def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb 

#background color for the program
backgroundColor = '#d3d3d3'

#main application
class application:
    def __init__(self, master):
        btnStart.destroy()


        #Frames  
        #The main frame      
        self.frame = Frame(master, bg=backgroundColor)
        self.frame.pack(side=LEFT, expand=TRUE, fill=BOTH)

        #The frame for the score at the right side of Question
        self.scoreFrame = Frame(master, bg=backgroundColor)
        self.scoreFrame.pack(side=RIGHT, expand=TRUE, fill=Y)

        #The frame for widgets to appear on the end page
        self.endPage = Frame(master, bg=backgroundColor)

        #variables and widgets
        #variable to move to the next question 
        self.i = 0

        #variable for calculating the points
        self.points = 0

        #points label that is going to appear on the right of the question
        self.scorePoints = Label(self.scoreFrame , text=('%d'%self.points), bg=backgroundColor, border=2, font=('', '30'), relief=RAISED, height=2,width=4)
        self.scorePoints.grid(sticky=E, pady=(85,105))

        #variable and label for the question
        self.question = list(Questions.keys())[self.i]
        self.questionLbl = Label(self.frame, text=self.question)
        self.questionLbl.grid(row=0,column=0, sticky=W, pady=(50,10))

        #entry widget for entering the answer
        self.answer = Entry(self.frame, highlightbackground='black')
        self.answer.grid(row=1, column=0, sticky=W, pady=(0,10), ipady=5)

        #button for moving to the next question
        self.btnNxt = Button(self.frame, text='Next', command=self.nxtBtn)
        self.btnNxt.grid(row=2, column=0, sticky=W, pady=(150, 0))

        #button for restarting the program that is going to appear on the bottom right of the question page
        self.btnReset = Button(self.scoreFrame, text='Reset', bg=backgroundColor, font=('', '14'), command=self.rstBtn)
        self.btnReset.grid(sticky=S)

        


        # appearance declaration for attributes in frame1
        for attribute in self.frame.winfo_children():
            attribute.configure(bg=backgroundColor, font=('', '15'))
            attribute.grid(padx=(30, 0))
       

    #function of next button       
    def nxtBtn(self):

        #if answer is correct then give two points
        if self.answer.get().lower().strip() == list(Questions.values())[self.i].lower():
            self.points += 2

        #if answer is not correct deduct 1 point
        else:
            self.points -= 1
        self.scorePoints.configure(text=('%d' %self.points))

        #move to the next question
        if self.i < len(Questions)-1:
            self.i+=1
            self.answer.delete(0, END)
            self.question = list(Questions.keys())[self.i]
            self.questionLbl.configure(text=self.question)

        # if no more questions are left then make the end page appear
        elif self.i >= len(Questions)-1:
            self.answer.delete(0, END)
            self.endPage.pack()
            self.scoreFrame.pack_forget()
            self.frame.pack_forget()
            levelAchieved = Label(self.endPage, text='', bg=backgroundColor, font=('', '20','bold'))
            levelAchieved.pack(pady=(50,10))

            # if result is less than 50% then print this onto the window
            if self.points < len(Questions):
                levelAchieved.configure(text='You need to do better!')

            # if result is more than 50% but less than 90% then print this
            elif self.points >= len(Questions) and self.points < (len(Questions)*2)*90/100:
                levelAchieved.configure(text='Well done!')

            # if result is more than or equal to 90% then print this
            elif self.points >= (len(Questions)*2)*90/100:
                levelAchieved.configure(text='Excellent!')

            #points scored printed onto the screen
            pointsScored = Label(self.endPage, text=('You scored %d points.'%self.points), bg=backgroundColor, font=('', '20'))
            pointsScored.pack(fill=Y)

            #reset button to reset the program
            btnReset = Button(self.endPage, text='Reset', bg=backgroundColor, font=('', '14'), command=self.rstBtn, width=20, height=3)
            btnReset.pack(pady=(20,0))




    #reset button to reset the program
    def rstBtn(self):
        #prompt
        askReset =messagebox.askyesno('Reset?','Are you sure?')

        #if user clicks yes then this happens
        if askReset > 0:
            #remove the end page and destroy every widget so that it does not appear the same next time
            for widget in self.endPage.winfo_children():
                widget.destroy()
            self.endPage.pack_forget()

            #reappear the main frame that holds the questions
            self.frame.pack(side=LEFT, expand=TRUE, fill=BOTH)
            #reappear the score main frame that is on the right of the question
            self.scoreFrame.pack(side=RIGHT, expand=TRUE, fill=Y)
            #set i and points back to 0
            self.i=0
            self.points=0
            #reset the question variable and label to current value of i that is 0
            self.question = list(Questions.keys())[self.i]
            self.questionLbl.configure(text=self.question)
            #reset the score variable to 0
            self.scorePoints.configure(text='%d'%self.points)

#gui declaration
root = Tk()
root.title('Quiz')
root.configure(background=backgroundColor)
#size of the window
root.geometry('500x400')
#removing resize capability of the program
root.resizable(0,0)

#Title of the program
programTitle = Label(root, text='Quiz', font=('', '20', 'bold'))
programTitle.pack(pady=10)

#function to start the program
def startBtn():
    frameRules.destroy()
    Quiz = application(root)


#rules for the game to appear at the start page
#frame for rules label
frameRules = Frame(root, relief='groove', border=5)
frameRules.pack(pady=30)

#label defining the rules
lblRules = Label(frameRules, text=("""Rules:
Total points are %d.
2 points on correct answer.
1 point deduction on wrong answer."""%(len(Questions)*2)), font=('','15'))
lblRules.pack(fill=BOTH, expand=TRUE)

#button to start the program
btnStart = Button(root, text='start', command=startBtn, width=15, height=3, font=('', '15'), border=('2px'))
btnStart.pack(pady=30)

#background color for every widget packed in root that is gonna appear at that the start page
for attribute in root.winfo_children():
    attribute.configure(bg=backgroundColor)

if __name__ == '__main__':
    root.mainloop()

