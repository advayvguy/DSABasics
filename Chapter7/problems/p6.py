import turtle
from GraphADT import Graph, Queue, Vertex

START = 'S'
OBSTACLE = '+'
TRIED = '.'
DEADEND = '-'
PART_OF_PATH = 'O'

#maze_file.readlines() returns a list of lines 

class Maze:
    def __init__(self, maze_filename): #youll give the mail filename when you initialize it
        with open (maze_filename,"r") as maze_file: #mazefile here is the file object
            self.maze_list = [[ch for ch in line.rstrip("\n")] for line in maze_file.readlines()]

        self.rows_in_maze = len(self.maze_list)
        self.coloums_in_maze = len(self.maze_list[0])

        #now to find the start position
        for rowid, row in enumerate(self.maze_list): #->enumerate does- (index, item)
            if START in row:
                self.start_row = rowid
                self.start_col = row.index(START)

        #in the maze, (0,0) is the top right coordinate, therfore we will be shifting the origin
        self.x_translate = -self.coloums_in_maze/2
        self.y_translate = self.rows_in_maze/2

        #now the turtle settings
        self.t = turtle.Turtle()
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(
            -(self.coloums_in_maze-1)/2 - 0.5,
            -(self.rows_in_maze-1)/2 - 0.5,
            (self.coloums_in_maze-1)/2 + 0.5,
            (self.rows_in_maze-1)/2 + 0.5
        ) 
        '''
            xmin,
            ymin,
            xmax,
            ymax
        '''

    def draw_maze(self):
        self.t.speed(10)
        self.wn.tracer(0) #draws the entire maze before displaying it
        for y in range(self.rows_in_maze):
            for x in range(self.coloums_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_centered_box(x + self.x_translate, -y + self.y_translate, "orange")
        self.t.color("black")
        self.t.fillcolor("blue") #affect the future draw operations
        self.wn.update()
        self.wn.tracer(1) #default settings

    def draw_centered_box(self, x, y, color):
        self.t.up()
        self.t.goto(x-0.5, y-0.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90) #facing north 
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def update_position(self, row, col, val=None):
        if val:
            self.maze_list[row][col] = val
        self.move_turtle(col, row)

        if val == PART_OF_PATH:
            color = "green"
        elif val == OBSTACLE:
            color = "red"
        elif val == TRIED:
            color = "black"
        elif val == DEADEND:
            color = "red"
        else:
            color = None

        if color:
            self.drop_bread_crumb(color)

    def move_turtle(self,col, row):
        self.t.up()
        self.t.setheading(self.t.towards(col + self.x_translate, -row + self.y_translate)) #face turtle in the direction of the coordinates
        self.t.goto(col + self.x_translate, -row + self.y_translate)
        
    def drop_bread_crumb(self, color):
        self.t.dot(10, color)

    def is_exit(self, row, col):
        return (
            row == 0
            or col == 0 
            or row == self.rows_in_maze - 1
            or col == self.coloums_in_maze - 1 
        ) #basically the boundary 
    
    def __getitem__(self, idx):
        return self.maze_list[idx]
    

'''
def search_from(maze, row, col):
    maze.update_position(row, col) #we move the turtle to the next position

    if maze[row][col] == OBSTACLE:
        return False
    
    if maze[row][col] in [TRIED, DEADEND]: #tried prevents infinite loops
        return False
    
    if maze.is_exit(row, col):
        maze.update_position(row, col, PART_OF_PATH)
        return True
    
    maze.update_position(row, col, TRIED) #to indicate that we tried this path

    found = (
        search_from(maze, row+1, col) #south
        or search_from(maze, row-1, col) #north
        or search_from(maze, row, col+1)
        or search_from(maze, row, col-1)
    )

    if found:
        maze.update_position(row, col, PART_OF_PATH)
    else:
        maze.update_position(row, col, DEADEND)

    return found
'''

def search_from_helper(maze, path_list, start_key):
    queue = Queue()
    queue.enqueue(start_key)
    while queue.size() > 0:
        current = queue.dequeue()
        row = current[0]
        col = current[1]  
        if maze.is_exit(row, col):
            maze.update_position(row, col, PART_OF_PATH)
            return current

        for neighbor in([(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]):          
            r = neighbor[0]
            c = neighbor[1]
            maze.update_position(r, c)
            if 0 <= r < maze.rows_in_maze and 0 <= c < maze.coloums_in_maze:
                if maze[r][c] in [TRIED, DEADEND, OBSTACLE]:
                    continue
                queue.enqueue(neighbor)
                maze.update_position(r, c, TRIED)
                path_list[neighbor] = current            


def search_from(maze, row, col):
    path_list = {}
    start = (row, col)
    current = search_from_helper(maze, path_list, (row, col))
    while current != start:
        r = current[0] 
        c = current[1]
        maze.update_position(r, c, PART_OF_PATH)
        current = path_list[current]
    maze.update_position(row, col, PART_OF_PATH)

my_maze = Maze("Chapter7/problems/maze.txt")
my_maze.draw_maze()
my_maze.update_position(my_maze.start_row, my_maze.start_col)

search_from(my_maze, my_maze.start_row, my_maze.start_col)
turtle.done()