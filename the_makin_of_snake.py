from score import Score_board
from turtle import *
import time
class Noname:
    def __init__(self):
        self.segment=[]
        self.screen=Screen()
        self.create()
        self.over=Score_board()
        
    def create(self):
        self.screen.tracer(0)
        for i in range(0,3):
            new_segment=Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(i*(-20),0)
            self.segment.append(new_segment)
        self.screen.update()    
        self.segment[0].shape("circle")
    def something(self):
        for i in range(len(self.segment)-1,0,-1):
            new_xco=self.segment[i-1].xcor()
            new_yco=self.segment[i-1].ycor()
            self.segment[i].goto(new_xco,new_yco)
                # print("herer")
            
        self.segment[0].forward(20)
        for i in range(1,len(self.segment)):
            if self.segment[0]==self.segment[i].pos():
                print(self.segment[i].pos())
                print("herer")
                
    def is_hit(self):
        if self.segment[0].xcor()>=300 or self.segment[0].xcor()<=-300 or self.segment[0].ycor()>=300 or self.segment[0].ycor()<=-300:
            
            self.speed(0)
            self.penup()
            self.color("white")
            self.goto(0,0)
            self.write(arg="Game Over",align="center",font=('Arial', 14, 'normal'))
            self.hideturtle()
            return False
                       
    def up(self):
        if self.segment[0].heading()==270:
            print("cant be done")
        else:    
            self.segment[0].setheading(90)
    def left(self):
        if self.segment[0].heading()==0:
            print("cant be done")
        else:
            self.segment[0].setheading(180)
    def down(self):
        if self.segment[0].heading()==90:
            print("cant be done")
        else:
            self.segment[0].setheading(270)
    def right(self):
        if self.segment[0].heading()==180:
            print("cant be done")
        else:
            self.segment[0].setheading(0)             
    def resrt(self):
        self.screen.tracer(0)
        for i in self.segment:
            i.goto(1000,1000)
        self.segment.clear()
        self.create()
        # for i in range(0,3):
        #     new_segment=Turtle("square")
        #     new_segment.color("white")
        #     new_segment.penup()
        #     new_segment.goto(i*(-20),0)
        #     self.segment.append(new_segment)
        # self.screen.update()    
        # self.segment[0].shape("circle")


    def extending(self):
        self.screen.tracer(0)
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        line=len(self.segment)
        

        new_segment.goto(self.segment[line-1].xcor(),self.segment[line-1].ycor())
        self.segment.append(new_segment)
        self.screen.update()

