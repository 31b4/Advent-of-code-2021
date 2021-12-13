def Read_all():
    lines = [[-1] + [int(x) for x in i] + [-1] for i in open('input.txt','r').read().split('\n')]
    return [[-1 for i in range(len(lines[0]))]] + lines + [[-1 for i in range(len(lines[0]))]]
def done(lines):
    for y in range(1,len(lines)-1):
        for x in range(1,len(lines[y])-1):
            if lines[y][x] > 9:
                return False
    return True

def Part1(lines):
    flashes = 0
    for i in range(100):
        for y in range(1,len(lines)-1):
            for x in range(1,len(lines[y])-1):
                lines[y][x] += 1
        while not done(lines):
            for y in range(1,len(lines)-1):
                for x in range(1,len(lines[y])-1):
                    if lines[y][x] > 9:
                        lines[y][x] = 0
                        flashes += 1
                        if lines[y+1][x+1] > 0: lines[y+1][x+1] += 1
                        if lines[y-1][x-1] > 0: lines[y-1][x-1] += 1
                        if lines[y+1][x-1] > 0: lines[y+1][x-1] += 1
                        if lines[y-1][x+1] > 0: lines[y-1][x+1] += 1
                        if lines[y+1][x] > 0: lines[y+1][x] += 1
                        if lines[y-1][x] > 0: lines[y-1][x] += 1
                        if lines[y][x+1] > 0: lines[y][x+1] += 1
                        if lines[y][x-1] > 0: lines[y][x-1] += 1
    return flashes
def Part2(lines):
    step = 0
    while True:
        step += 1
        flashes = 0
        for y in range(1,len(lines)-1):
            for x in range(1,len(lines[y])-1):
                lines[y][x] += 1
        while not done(lines):
            for y in range(1,len(lines)-1):
                for x in range(1,len(lines[y])-1):
                    if lines[y][x] > 9:
                        lines[y][x] = 0
                        flashes += 1
                        if lines[y+1][x+1] > 0: lines[y+1][x+1] += 1
                        if lines[y-1][x-1] > 0: lines[y-1][x-1] += 1
                        if lines[y+1][x-1] > 0: lines[y+1][x-1] += 1
                        if lines[y-1][x+1] > 0: lines[y-1][x+1] += 1
                        if lines[y+1][x] > 0: lines[y+1][x] += 1
                        if lines[y-1][x] > 0: lines[y-1][x] += 1
                        if lines[y][x+1] > 0: lines[y][x+1] += 1
                        if lines[y][x-1] > 0: lines[y][x-1] += 1
        
        if flashes == 100:
            return step
lines = Read_all()
print("part 1: ",Part1(lines))
lines = Read_all()
print("part 2: ",Part2(lines))
