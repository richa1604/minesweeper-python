from tkinter import Button
import random
import settings
class Cell:
    all=[]
    def __init__(self,x,y,is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object=None
        self.x=x
        self.y=y

        #append the object to cell.all list
        Cell.all.append(self)

    def create_btn_object(self,location):
        btn=Button(
            location,
            width=12,
            height=4,
            text=f"{self.x},{self.y}"
        )
        btn.bind('<Button-1>',self.left_click_action) #button-1 is for
        #for left click for right its -3
        btn.bind('<Button-3>',self.right_click_action)
        self.cell_btn_object=btn
    def left_click_action(self,event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()
    def show_mine(self):
        #a logic to interrupt the gameand display the message that playerlost
        self.cell_btn_object.configure(bg='red')
    def show_cell(self):
        pass


    def right_click_action(self,event):
        print(event)
        print("right click")
    @staticmethod
    def random_mines():
        picked_cells=random.sample(
            Cell.all,settings.MINE_COUNT

        )
        for picked_cell in picked_cells:
            picked_cell.is_mine=True


    def __repr__(self):
        return f"Cell({self.x},{self.y})"
    
    

