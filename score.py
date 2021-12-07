import time
from turtle import Turtle, mode
class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.count=0 
        self.speed(0)
        self.penup()
        self.color("white")
        self.goto(0,260)
        self.write(arg=f"score: {self.count}",align="center",font=('Arial', 14, 'normal'))
        
        self.hideturtle()
        self.clear()
        # self.highScore=0
        with open("score.txt") as file:
            self.highScore=int(file.read())
            
            # self.highScore=tio
        # self.hio()
        # if self.count>=1:
            
        #     self.clear()
    def hio(self):
        self.clear()
        
        self.goto(0,260)

        
        self.write(arg=f"score: {self.count} H.S: {self.highScore}",align="center",font=('Arial', 14, 'normal'))
        self.count+=1
        
    def over(self):
        if self.count>self.highScore:
            with open("score.txt",mode="w")as file:

                file.write(f"{self.count}")
            self.highScore=self.count
        
        self.hio()    
        self.goto(0,0)
        self.write(arg="Game Over",align="center",font=('Arial', 14, 'normal'))
        time.sleep(2)
        self.count=0
        self.clear()

        
        
            

        