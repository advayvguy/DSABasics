import turtle
import random

def tree(branchlen,thickness, t, max):
    if branchlen <= 25:
        t.color("DarkGreen")
    if branchlen > 5:
        t.width(thickness*(branchlen/max))
        color_state = t.pencolor()
        t.forward(branchlen)
        a1 = random.randrange(15,45)
        a2 = random.randrange(30,90)
        t.right(a1)
        tree(branchlen - random.randrange(10, 25), thickness, t, max)
        t.left(a2)
        tree(branchlen - random.randrange(10, 25), thickness, t, max)
        t.color(color_state)
        t.width(thickness*(branchlen/max))
        t.right(a2 - a1)
        t.backward(branchlen)

def main():
    t = turtle.Turtle()
    win = turtle.Screen()
    t.color("saddlebrown")
    t.width(10)
    t.left(90)
    t.penup()
    t.backward(200)
    t.pendown()
    tree(130,20,t,130)
    win.exitonclick()

main()
