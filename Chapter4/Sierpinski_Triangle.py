import turtle

#points is a 2d array 

def draw_triangle(points, color, t):
    t.fillcolor(color)
    t.up()
    t.goto(points[0][0], points[0][1])
    t.down()
    t.begin_fill()
    t.goto(points[1][0], points[1][1])
    t.goto(points[2][0], points[2][1])
    t.goto(points[0][0], points[0][1])
    t.end_fill()

def mid(p1,p2):
    return ((p1[0]/2 + p2[0]/2), (p1[1]/2 + p2[1]/2))

def fun_triangle(points, color_p, t):

    colors = [
    "pink",
    "white",
    "yellow",
    "green",
    "blue",
    "red",
    ]

    if color_p < 6:
        draw_triangle(points, colors[color_p], t)
        fun_triangle([mid(points[0],points[1]), points[1], mid(points[1], points[2])],
                        color_p + 1, t)
        fun_triangle([mid(points[1],points[0]), points[0], mid(points[0], points[2])],
                        color_p + 1, t)
        fun_triangle([mid(points[0],points[2]), points[2], mid(points[2], points[1])],
                        color_p + 1, t)

def main():
    t = turtle.Turtle()
    win = turtle.Screen()
    points = [[-180,-150], [0,150], [180, -150]]
    fun_triangle(points, 0, t)
    win.exitonclick()

main()
