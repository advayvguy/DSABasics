import turtle 

def hilbert_curves(level, size, t, angle):
    if level == 0:
        t.left(180)
        return 
    t.right(angle)
    hilbert_curves(level-1, size, t, -angle)
    t.right(angle)
    t.forward(size)
    hilbert_curves(level-1, size, t, angle)
    t.left(angle)
    t.forward(size)
    t.left(angle)
    hilbert_curves(level-1, size, t, angle)
    t.forward(size)
    t.right(angle)
    hilbert_curves(level-1, size, t, -angle)
    t.right(angle)


def main():
    t = turtle.Turtle()
    win = turtle.Screen()
    t.left(90)
    t.speed(0)
    hilbert_curves(4, 20, t, 90)
    win.exitonclick()

main()