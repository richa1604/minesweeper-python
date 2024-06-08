from tkinter import *
import settings
import utilis
from cell import Cell
"""the below code is for the table"""
root=Tk()
#over rise the setting of the window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper game")
root.resizable(False,False)

top_frame=Frame( 
    root,
    bg="black", #change to black
    width=settings.WIDTH,
    height=utilis.height_prct(25)
 )
top_frame.place(x=0,y=0)
"""in order to specify where the particular
frame should start we need to give
x axis and y axis details to the toop
frame placement"""

left_frame=Frame(
    root,
    bg='black',
    width=utilis.width_prct(25),
    height=utilis.height_prct(75),  #720-180
)
left_frame.place(x=0,y=utilis.height_prct(25))
center_frame=Frame(
    root,
    bg='black',
    width=utilis.width_prct(75),
    height=utilis.height_prct(75)
)  
center_frame.place(
    x=utilis.width_prct(25),
    y=utilis.height_prct(25)
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):  #this will create 25 cells
        c=Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
        column=x,row=y
        )

print(Cell.all)
Cell.random_mines = ()
for c in Cell.all:
    print(c.is_mine)
#run the window
root.mainloop()
"""now we configure the frame=most basic elemet
we can create in a window
divide the section of the window for
different elements """




