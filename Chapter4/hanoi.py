'''
    there are three basic rules to solving the tower of hanoi problem
    1st- move h-1 to the int_pole
    2nd- move heaviest peg to the to_pole
    3rd- move h-1 to the to_pole
'''

count = 1

def move_tower(pegs, from_pole, int_pole, to_pole):
    if pegs >= 1:
        move_tower(pegs-1, from_pole, to_pole, int_pole)
        move_disk(from_pole, to_pole)
        move_tower(pegs-1, int_pole, from_pole, to_pole)

def move_disk(from_pole, to_pole):
    global count
    print(f"{count:5d} : moving disk from {from_pole} to {to_pole}")
    count = count + 1

move_tower(2, "A", "B", "C")

