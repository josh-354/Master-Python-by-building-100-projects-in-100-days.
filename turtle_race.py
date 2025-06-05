from turtle import Turtle,Screen
import random

is_race_on=False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="make your bet",prompt="which color will win,choose a color")
x_position = -200
y_position = -150
color = ["red", "blue", "yellow", "green", "orange", "purple", "pink", "brown", "cyan"]


turtle=[]


def create_turtle(color_list,x_pos,y_pos):
    t = Turtle(shape=("turtle"))
    t.color(random.choice(color))
    t.penup()
    t.goto(x=x_position,y=y_position)

    return t

for n in range(8):
     t = create_turtle(color,x_position,y_position)
     turtle.append(t)
     y_position += 50

if user_bet:
     is_race_on = True

while is_race_on:
     for t in turtle:
        random_distance = (random.randint(0,10))
        t.forward(random_distance)

        if t.xcor()>230:
            is_race_on=False
            winning_color = t.pencolor()
            if winning_color == user_bet.lower():
                print(f"you chose {winning_color}, YOU WIN")
            else:
                print("you lose")
            


screen.exitonclick()
