import turtle 

def koch(t, size, depth):
    if depth == 0:
        t.forward(size)
        return 
    size /= 3
    koch(t, size, depth-1)
    t.left(60)
    koch(t, size, depth-1)
    t.right(120)
    koch(t, size, depth-1)
    t.left(60)
    koch(t, size, depth-1)

def koch_snowlake(t, size, depth):
    for _ in range(3):
        koch(t, size, depth)
        t.right(120)

def main():
    t = turtle.Turtle()
    win = turtle.Screen()
    t.speed(0)
    t.color("light blue")
    t.fillcolor("light sky blue")
    t.begin_fill()
    koch_snowlake(t, 500, 4)
    t.end_fill()
    win.exitonclick()

main()