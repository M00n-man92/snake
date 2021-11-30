from turtle import *
import time
class Noname:
    def __init__(self):
        self.segment=[]
        self.screen=Screen()
        self.create()
        
    def create(self):
        self.screen.tracer(0)
        for i in range(0,3):
            new_segment=Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(i*(-20),0)
            self.segment.append(new_segment)
        self.screen.update()    

    def something(self):
        for i in range(len(self.segment)-1,0,-1):
            new_xco=self.segment[i-1].xcor()
            new_yco=self.segment[i-1].ycor()
            self.segment[i].goto(new_xco,new_yco)
                # print("herer")
            
        self.segment[0].forward(20)
        # self.segment[0].left(90)
        # self.segment[0].forward(20)
    def up(self):
        self.segment[0].setheading(90) 
    # def down(self):
    #     self.segment[0].left(180)
    # def left(self):
    #     self.segment[0].left(279)
    # def right(self):
    #     self.segment[0].left(0)              
