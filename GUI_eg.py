from tkinter import *
window = Tk()
window.geometry("800x800")
window.title("Abhinand")
window.configure(bg="#3EB67A")

def button_action():
    print("You clicked the OK ENTER button-")

def button_action2():
    print("Cancelled")

button = Button(window,text = "ENTER",width = 8,height=1,fg="black",command=button_action)
button2 = Button(window,text="CANCEL",width=8,height=1,fg="black",command=button_action2)
label = Label(window,text = "OK",bg="black",fg="white")

button.grid(row=0,column=0)
button2.grid(row=2,column=1)

window.mainloop()
print("END")