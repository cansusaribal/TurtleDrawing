
import turtle
import random
import time

window = turtle.Screen()
window.title("Catch the Turtle Game")
window.bgcolor("SlateBlue")

t = turtle.Turtle()
t.shape("turtle")
t.shapesize(stretch_wid=2, stretch_len=2)
t.color("LavenderBlush")
t.penup()
t.speed(0)

score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(-350, 200)
score_turtle.write("Skor: 0", align="left", font=("Verdana", 50, "normal"))

timer_turtle = turtle.Turtle()
timer_turtle.hideturtle()
timer_turtle.penup()
timer_turtle.goto(120, 200)

score = 0

time_limit = 60

def update_score():
    score_turtle.clear()
    score_turtle.write(f"Skor: {score}", align="left", font=("Verdana", 50, "normal"))

def catch_turtle(x, y):
    global score
    score += 1
    update_score()
    move_turtle()

def move_turtle():
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.goto(x, y)

def countdown(time_left):
    if time_left > 0:
        timer_turtle.clear()
        timer_turtle.write(f"Süre: {time_left}", align="left", font=("Verdana", 50, "normal"))
        window.ontimer(lambda: countdown(time_left - 1), 1000)
    else:
        end_game()

def end_game():
    t.hideturtle()
    timer_turtle.clear()
    timer_turtle.goto(0, 0)
    timer_turtle.write(f"Oyun Bitti! Skorunuz: {score}", align="center", font=("Verdana", 50, "bold"))

t.onclick(catch_turtle)

move_turtle()

countdown(time_limit)

window.mainloop()