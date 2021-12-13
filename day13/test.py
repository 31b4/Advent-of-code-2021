with open("input.txt") as f:
    file, folds = f.read().split("\n\n")
    folds = [x.split(" ")[-1].split("=") for x in folds.splitlines()]
    file = [list(map(int, x.split(","))) for x in file.splitlines()]
maxX =0
maxY = 0
for x, y in file:
    if x>maxX:
        maxX = x
    if y > maxY:
        maxY = y
grid = [[" " for _ in range(maxX)] for _ in range(maxY)]


def calc_folds(folds, x, y):
    for fold in folds:
        if fold[0] == "x":
            x = int(fold[1]) - abs(int(fold[1]) - x)
        else:
            y = int(fold[1]) - abs(int(fold[1]) - y)
    return x, y


for x, y in file:
    a, b = calc_folds(folds, x, y)
    grid[b][a] = "#"


count = 0
for row in grid:
    count += row.count("#")
    print(row)
print(count)