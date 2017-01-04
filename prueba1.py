from tkinter import *
import sys

tk = Tk()
canvas = Canvas(tk, width=800, height=800)#ventana
canvas.pack()
x=10
y=300

imagPelota=PhotoImage(file="ball.gif")
canvas.create_image(x,y,anchor=NW,image=imagPelota)

my_image=PhotoImage(file="arco3.gif")
canvas.create_image(400,200,anchor=NW,image=my_image)
print("cordenada x\t cordenada y")
def moverpelota(event):
    global x
    global y

 

    if event.keysym == 'Left':
         
         canvas.move(1, -3, 0)
         x=x-3
         print(x,"\t\t",y)
    elif event.keysym == 'Right':
         
         canvas.move(1, 3, 0)
         x=x+3
         print(x,"\t\t",y)

         if(x==400):
             print("GOOOOOOOOOOOLL")
             sys.exit(0)
            


#canvas.bind_all('<KeyPress-Up>', moverpelota)
#canvas.bind_all('<KeyPress-Down>', moverpelota)
canvas.bind_all('<KeyPress-Left>', moverpelota)
canvas.bind_all('<KeyPress-Right>', moverpelota)
tk.mainloop()
