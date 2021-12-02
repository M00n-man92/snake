from turtle import Turtle
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
    def hio(self):
        
        self.clear()

        
        self.write(arg=f"score: {self.count}",align="center",font=('Arial', 14, 'normal'))
    def over(self):
        
        self.goto(0,0)
        self.write(arg="Game Over",align="center",font=('Arial', 14, 'normal'))