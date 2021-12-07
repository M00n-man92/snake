
from turtle import *
import time
from the_makin_of_snake import Noname 
from food import Food
from score import Score_board
screen=Screen()
score=Score_board()
screen.bgcolor("black")
snake=Noname()
food=Food()

game=True
screen.tracer(0)

screen.setup(width=600,height=600)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
score
# screen.onkey(key="downp",fun=snake.down())
# screen.onkey(key="left",fun=snake.left())
# screen.onkey(key="right",fun=snake.right())
while game:
    screen.update()
    time.sleep(0.1)
    snake.something()
    # game=snake.collison()
    if snake.segment[0].distance(food)<15:
        food.another_one()
        
        
        score.hio()
        snake.extending()
        

    if snake.segment[0].xcor()>=300 or snake.segment[0].xcor()<=-300 or snake.segment[0].ycor()>=300 or snake.segment[0].ycor()<=-300:
        score.over()
        snake.resrt()
         
    
    
    for i in snake.segment[1:]:
        
        
        if snake.segment[0].distance(i) < 15:
            
         
            
            score.over()
            score.hio()
            time.sleep(1)
            snake.resrt()
    # for i in range(1,len(snake.segment)):
    #     likn=[]
    #     likn.append(snake.segment[i].pos())
    # for j in range(0,len(likn)-1):
    #     if snake.segment[0].pos()==likn[i]:
    #         score.over()
    #         game=False
    #     else:
    #         likn.clear()                      
        

screen.exitonclick()
screen.listen()