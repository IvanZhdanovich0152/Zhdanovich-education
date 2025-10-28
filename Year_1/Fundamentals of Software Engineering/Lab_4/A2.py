n,m = map(int, input().split())


def draw_rectangle(rows, columns, char = "#"):
    for i in range(rows):
        for j in range(columns):
            print(char, end='')
        print()
    print()

def draw_triangle(rows, columns, char = "#"):
    for i in range(rows):
        for j in range(columns):
            if i >= j:
                print(char, end='')
            else:
                continue
        print()
    print()

def draw_ramka(rows, columns, char = "#"):
    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == rows - 1:
               print(char, end='')
            elif j == 0 or j == columns - 1:
                print(char, end='')
            else:
                print(" ", end='')
        print()
    print()


draw_rectangle(n, m, char="*")
draw_triangle(n,m, char="1")
draw_ramka(n,m)