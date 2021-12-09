def Read_all():
    with open("input.txt") as f:
        return f.read().split('\n')

def Part1(lines):
    summ = 0
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
    return summ
def Part2(lines):
    pass


lines = Read_all()
print("part 1: ", Part1(lines))
print("part 2: ", Part2(lines))
