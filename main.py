from turtle import *
import time
from the_makin_of_snake import Noname 
screen=Screen()
screen.bgcolor("black")
snake=Noname()

game=True
screen.tracer(0)


screen.listen()
screen.onkey(snake.up, "Up")
   
# screen.onkey(key="downp",fun=snake.down())
# screen.onkey(key="left",fun=snake.left())
# screen.onkey(key="right",fun=snake.right())
while game:
    screen.update()
    time.sleep(0.1)
    snake.something()

   
        
screen.setup(width=600,height=500)
screen.exitonclick()
screen.listen()