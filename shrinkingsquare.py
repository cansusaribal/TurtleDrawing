import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("Turtle python")

turtle_instance=turtle.Turtle()
turtle_instance.color("blue")

def shrinkingSqaure(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)

shrinkingSqaure(150)
shrinkingSqaure(100)
shrinkingSqaure(50)
turtle.done()
