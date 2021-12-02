
from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self) :
        self.count=0
        super(). __init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.6,stretch_wid=0.6)
        
        self.color("yellow")
        self.penup()
        self.another_one()
       
    def another_one(self):
        
        randx=random.randrange(-290,290)
        randy=random.randrange(-290,290)
        
        self.goto(randx,randy)

        
    
