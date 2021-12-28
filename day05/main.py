import re
def Read_all():
    with open("input.txt") as f:
        return f.readlines()
def MatrixGenerate():
    matrix = []
    for i in range(1000):
        sv=[]
        for j in range(1000):
            sv.append(0)
        matrix.append(sv)
    return matrix
def Count_dangerous(matrix):
    counter = 0
    for line in matrix:
        for num in line:
            if num >1:
                counter +=1
    return counter
def Part1(lines,matrix):
    for line in lines:
        x1, y1, x2, y2 = map(int, re.match(r'(\d+),(\d+) -> (\d+),(\d+)', line).groups()) 
        if x1 == x2:#vertical fill
            if y1>y2:
                for i in range(y2,y1+1):
                    matrix[i][x1] +=1
            else:
                for i in range(y1,y2+1):
                    matrix[i][x1] +=1
        elif y1==y2:#horizontal fill
            if x1>x2:
                for i in range(x2,x1+1):
                    matrix[y1][i] +=1
            else:
                for i in range(x1,x2+1):
                    matrix[y1][i] +=1
    return matrix
def Part2(lines,matrix):
    for line in lines:
        x1, y1, x2, y2 = map(int, re.match(r'(\d+),(\d+) -> (\d+),(\d+)', line).groups())
        if x1 == x2:#vertical fill
            if y1>y2:
                for i in range(y2,y1+1):
                    matrix[i][x1] +=1
            else:
                for i in range(y1,y2+1):
                    matrix[i][x1] +=1
        elif y1==y2:#horizonzal fill
            if x1>x2:
                for i in range(x2,x1+1):
                    matrix[y1][i] +=1
            else:
                for i in range(x1,x2+1):
                    matrix[y1][i] +=1
        elif (x1==y2 and x2==y1) or x1-x2==y1-y2 or abs(x1-x2)==abs(y1-y2):
        #diagonal fill
            for i in range(abs(x1-x2)+1):
                if y1<y2 and x1>x2:
                    matrix[y1+i][x1-i] +=1
                elif x1<x2 and y1>y2:
                    matrix[y1-i][x1+i] +=1
                elif x1<x2 and y1<y2:
                    matrix[y1+i][x1+i] +=1
                elif x1>x2 and y1>y2:
                    print(x1-i,y1-i)
                    matrix[y1-i][x1-i] +=1
      
    return matrix





lines = Read_all()
matrix = MatrixGenerate()
matrix = Part1(lines,matrix)
print("part 1: ",Count_dangerous(matrix))
matrix2 = MatrixGenerate()
matrix2 = Part2(lines,matrix2)
print("part 2: ",Count_dangerous(matrix2))
