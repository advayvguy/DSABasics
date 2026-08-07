TITLE_Y = 400
LABEL_Y = -50
POLE_SPACING = 300
PUCK_HEIGHT = 20 
ROD_LEN = 350
import turtle
from ADT import Stack

def draw_rectangle(x1, y1, x2, y2, color, t):
    t.penup()
    t.goto(x1,y1)
    t.fillcolor(color)
    t.begin_fill()
    t.pendown()
    for x,y in [(x2, y1), (x2, y2), (x1, y2), (x1, y1)]:
        t.goto(x,y)
    t.end_fill()

def clear_rectangle(x1, y1, x2, y2, t):
    old_color = t.pencolor()
    t.pencolor("white")
    t.fillcolor("white")
    t.penup()
    t.begin_fill()
    t.goto(x1,y1)
    t.pendown()
    for x,y in [(x2, y1), (x2, y2), (x1, y2), (x1, y1)]:
        t.goto(x,y)
    t.end_fill()
    t.pencolor(old_color)

def draw_line(x1, x2, y, t):
    t.penup()
    t.goto(x1,y)
    t.pendown()
    t.goto(x2,y)

class Pole:
    def __init__(self, multiplier, center, thickness, label):
        self.mult = multiplier #for the width of the rectangle
        self.num_stack = Stack() 
        self.t = turtle.Turtle() #every pole has its own turtle
        self.center = center #pole x coordinate
        self.top = 0 #y coordinate of the topmost point
        self.puck_thickness = thickness
        self.t.penup()
        self.t.goto(center, LABEL_Y)
        self.t.write(label, align="center", font=("Arial", 20, "bold"))
        self.t.pendown()

        self.colors = [
            None,           # index 0 unused
        "#E63946",      # red
        "#F4A261",      # orange
        "#E9C46A",      # gold
        "#2A9D8F",      # teal
        "#457B9D",      # blue
        "#6A4C93",      # purple
        "#FF006E",      # magenta
        "#06D6A0",      # mint
        "#118AB2",      # cyan
        "#8AC926",      # lime
        ]

        self.t.penup()
        self.t.goto(center, 0)
        self.t.pendown()
        self.t.goto(center, ROD_LEN)

    def add_pole(self, num):
        self.num_stack.push(num)
        color = self.colors[num]
        draw_rectangle(self.center + (num*self.mult), self.top, self.center - (num*self.mult), self.top + self.puck_thickness, color, self.t)
        self.top = self.top + self.puck_thickness

    def remove_pole(self):
        num = self.num_stack.pop()
        clear_rectangle(self.center + (num*self.mult), self.top, self.center - (num*self.mult), self.top - self.puck_thickness, self.t)
        self.top = self.top - self.puck_thickness
        if self.num_stack.is_empty():
            next_num = 0
        else:
            next_num = self.num_stack.peek()
        draw_line(self.center + (next_num*self.mult), self.center - (next_num*self.mult), self.top, self.t)
        self.t.penup()
        self.t.goto(self.center, self.top)
        self.t.pendown()
        self.t.goto(self.center, self.top + self.puck_thickness)
        return num

def hanoi(from_pole, to_pole, int_pole, n):
    if n < 1:
        return
    hanoi(from_pole, int_pole, to_pole, n-1)
    num = from_pole.remove_pole()
    to_pole.add_pole(num)
    hanoi(int_pole, to_pole, from_pole, n-1)


def main():
    t = turtle.Turtle()
    win = turtle.Screen()
    t.penup()
    t.goto(0, TITLE_Y)
    t.write("TOWER OF HANOI", align="center", font=("Arial", 30, "bold"))
    from_pole = Pole(20, 0, PUCK_HEIGHT, "from pole")
    to_pole = Pole(20, POLE_SPACING, PUCK_HEIGHT, "to pole")
    int_pole = Pole(20, -POLE_SPACING, PUCK_HEIGHT, "helper pole")
    for i in range(6,0,-1):
        from_pole.add_pole(i)
    hanoi(from_pole, to_pole, int_pole, 6)
    win.exitonclick()

main()