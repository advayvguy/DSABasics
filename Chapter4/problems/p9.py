from ADT import Stack

def hanoi(n, to_pole, from_pole, int_pole):
    if n == 1:
        to_pole.push(from_pole.pop())
        return
    hanoi(n-1, int_pole, from_pole, to_pole)
    to_pole.push(from_pole.pop())
    hanoi(n-1, to_pole, int_pole, from_pole)

def main():
    to_pole = Stack()
    from_pole = Stack()
    int_pole = Stack()
    for i in range(5,0,-1):
        from_pole.push(i)
    hanoi(5, to_pole, from_pole, int_pole)
    for i in range(0,5):
        print(to_pole.pop())

main()