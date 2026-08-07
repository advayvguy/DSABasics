from math import factorial as fact

def pascal_triangle(n, width):
    if n == 1:
        return
    pascal_triangle(n-1, width)
    line = ""
    for i in range(0, n+1):
        term = fact(n)/(fact(i)*fact(n-i))
        line = line + f"{str(int(term)):^6}" 
    print(f"{line:^{width}}\n")

def find_width(n):
    line = ""
    for i in range(0, n+1):
        term = fact(n)/(fact(i)*fact(n-i))
        line = line + f"{str(int(term)):^6}"
    return len(line)

def main():
    n = 13
    width = find_width(n)
    print(f"\n{1:^{width}}\n")
    pascal_triangle(n, width)
main()