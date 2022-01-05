from tkinter import *
root = Tk()
root.title("MultiDimensional Arrays")
root.geometry("500x500")

label = Label(root)

array1d = ["John", "Flash", "Mark"]
print(array1d[0])

array2d = [["John", "A"], ["Flash","B"], ["Mark","C"]]
print(array2d[0][1])

array3d =[[["John" , "A" , "Excellent"], ["Flash", "B","Very good"], ["Mark", "C", "Good"]]]
print(array3d[0][0][2])

def report():
    label["text"] = array3d[0][1][0] + " got grade " + array3d[0][0][1] + " and he is doing " + array3d[0][0][2]

btn = Button(root, text = "show report", command=report)
btn.place(relx = 0.5, rely = 0.5, anchor=CENTER)

label.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()