from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mbox
import shutil

import os
import pygame
from pydub import AudioSegment

import subprocess
root=Tk()
#root.geometry('320x175')
root.title('MP3 Player')
root.resizable(0,0)
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))



dir =  os.path.join(os.path.expanduser('~'), 'new')
if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)



#file dialog function
#-----------------------------------------
audio_file_name=''
song =''
listofsongs=[]
index=0
gimg=PhotoImage(file='pause.png')
text="01101100"

text = (' '*20) + text + (' '*20)
def directorychooser():
    	
    global audio_file_name
    global song
    global listofsongs
    global index
    global marquee
    global text
    audio_file_name = subprocess.check_output(["zenity", "--file-selection"]).decode("utf-8").strip() 
    
     
    
    if audio_file_name:
		
        try:
            mtw=AudioSegment.from_mp3(audio_file_name)
            mtw.export("{0}/new.wav".format(dir),format="wav")
				
            pygame.mixer.init()
            pygame.mixer.music.load("{0}/new.wav".format(dir))
            pygame.mixer.music.play()

        except:
            mbox.showerror('Error', "Please input an mp3 file")
            
    

            
            


  
class mixerWrapper():

    def __init__(self):
        self.IsPaused = False

    def toggleMusic(self):
        try:
            if self.IsPaused:
                pygame.mixer.music.unpause()
                self.IsPaused = False
            else:
                pygame.mixer.music.pause()
                self.IsPaused = True
        except:
            pass

mtoggle=mixerWrapper()
def rwind():
    try:
        pygame.mixer.music.play()
    except:
        directorychooser()


#-----------------------------------------
   
			
#Menu defined
#----------------------------------------------
menu=Menu(root)
root.config(menu=menu)
subMenu=Menu(menu,tearoff=0)


menu.add_cascade(label="Media",menu=subMenu)
subMenu.add_command(label='Open....',command=lambda:directorychooser())
subMenu.add_command(label='Exit.....',command=root.destroy)

#-frames defined------------------------------------------------
frm1=Frame()
frm2=Frame()

#buttons defined...............................................
marquee=Text(frm1,bg='black',width=35,height=11,relief=SUNKEN,fg='red',font=('','15'),state='normal')
marquee.bind("<Key>", lambda e: "break")

pauseimg=PhotoImage(file='pause.png')
playbutton=PhotoImage(file='play-button.png')
previousimg=PhotoImage(file='previousimg.png')

marquee.pack()


i = 0

def command(x, i):
    marquee.insert("1.1", '|'+x)
    #marquee.config(text=x+x+x)
    if i == len(text):
        i = 0
    else:
        i = i+1
    root.after(100, lambda:command(text[i:i+20], i))

command(text[i:i+20], i)


btnplay=Button(frm2,image=playbutton,command=directorychooser)
btnplay.pack(side=LEFT)

btnpause=Button(frm2, image=pauseimg,command=mtoggle.toggleMusic)
btnpause.pack(side=LEFT)

btnpre=Button(frm2, image=previousimg,command=rwind)
btnpre.pack(side=LEFT)




frm1.pack()
frm2.pack()


root.mainloop()
