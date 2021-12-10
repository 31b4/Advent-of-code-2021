import numpy as np
def Read_all():
    with open("input.txt") as f:
        return f.read().split('\n')

def Part1(lines):
    summ = 0
    lows = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            notSafe =  False
            current = int(lines[i][j])
            if current == 9:
                notSafe = True
            if i > 0:
                if int(lines[i - 1][j]) < current:
                    notSafe = True
            if j > 0:
                if int(lines[i][j - 1]) < current:
                    notSafe = True
            if j < (len(lines[i]) - 1):
                if int(lines[i][j + 1]) < current:
                    notSafe = True
            if i < (len(lines) - 1):
                if int(lines[i + 1][j]) < current:
                    notSafe = True
            if not notSafe:
                print(current)
                summ += 1 + int(current)
                lows.append((i,j))
    return lows, summ
def Part2(lines,lows):
    current_id = 0
    for row,col in lows: #Depth-first search
        current = [(row,col)]
        visited = set()
        while len(current) > 0:
            row, col = current.pop()
            if (row,col) in visited:
                continue
            visited.add((row,col))
            ids[row,col]= current_id

lines = Read_all()
lows, ans1 = Part1(lines)
print(lows)
print("part 1: ", ans1)
print("part 2: ", Part2(lines,lows))
