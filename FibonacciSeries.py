import sys
from tkinter import *

#defining all sub-routiens
def speak():
   # pass #Write the required button code here
   txt.config(state=NORMAL)
   txt.delete(0.0, 'end')
   txt.config(state=DISABLED) 
   number = ent.get()
   print(number)
   c = 0
   d = 1
   sum = 0
   stringDisp = "0 \n"
   for x in range (0, int(number)):
        txt.config(state=NORMAL) #Enabling the editing option for textbox to fill in the required text
        sum = c + d
        print(sum)
        stringDisp += (str(sum))
        stringDisp += ("\n")
        if(x == int(number) -1):
            txt.insert(0.0, stringDisp)            
        txt.config(state=DISABLED) #Disabling the editing option for textbox
        d = c
        c = sum  
#Start the root...
main = Tk()

#Set the params root:
main.title("Fibonacci Series")
main.geometry("400x350")

#Adding a frame:
GUIFrame = Frame(main)
GUIFrame.grid(row = 0, column = 0, sticky = W)

#Adding a label
Label(GUIFrame, text="Number of terms:").grid(row=0, column = 0, sticky=W)


#Add a button
Button(GUIFrame, text = "Compute", width = 6, command = speak).grid(row= 1, column = 0, sticky = W)

#Adding a frame


#Adding a texxtbox
ent = Entry(main)
ent.grid(row = 0, column = 1)
txt = Text(main, width = 20, height = 20, borderwidth = 2, relief = "sunken")
txt.grid(row = 0, column = 2, sticky = W)
txt.config(state=DISABLED)

#Kickstart the loop
main.mainloop()
#main.grid(row=, column=, sticky=W)

