def Read_all():
    with open("input.txt") as f:
        cords, folds = f.read().split("\n\n")
        folds = [x.split(" ")[-1].split("=") for x in folds.splitlines()]
        cords = [list(map(int, x.split(","))) for x in cords.splitlines()]
        return cords,folds


def calc_folds(folds, x, y):
    for fold in folds:
        if fold[0] == "x":
            x = int(fold[1]) - abs(int(fold[1]) - x)
        else:
            y = int(fold[1]) - abs(int(fold[1]) - y)
    return x, y        

def GridMake(cords):
    grid = []
    maxX =0
    maxY = 0
    print(cords)
    for x, y in cords:
        if x>maxX:
            maxX = x
        if y > maxY:
            maxY = y
    for i in range(maxY+1):
        sv = []
        for j in range(maxX+1):
            sv.append(' ')
        grid.append(sv)
    for x,y in cords:
        grid[y][x] = "#"        
    return grid



cords,folds = Read_all()

grid = GridMake(cords)
for line in grid:
    print(line)
print("part 1: ",)

