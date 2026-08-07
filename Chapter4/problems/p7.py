import turtle  

def fractal(t, side_len, maxlen):
    if side_len <= 10:
        return 
    t.left(60)
    t.forward(side_len/4)
    fractal(t,side_len/2, maxlen)
    t.forward(side_len/4)
    t.right(120)
    t.forward(side_len/4)
    fractal(t, side_len/2, maxlen)
    t.forward(side_len/4)
    t.left(60)
    if maxlen == side_len:
        t.right(180)
        t.forward(side_len/4)
        fractal(t, side_len/2, maxlen)
        t.forward(side_len/4)

def main():
    t = turtle.Turtle()
    win = turtle.Screen()
    t.color("black")
    side_len = 400
    fractal(t, side_len, side_len)
    win.exitonclick()

main()