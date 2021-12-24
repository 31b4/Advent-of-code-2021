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
                summ += 1 + int(current)
                lows.append((i,j))
    return lows, summ
def Part2(lines,lows):
    pools = []
    for x,y in lows:
        opens = [[x,y]]
        closes = []
        while len(opens) > 0:
            cX = opens[0][0]
            
            cY = opens[0][1] #jelenlegi pos
            closes.append(opens[0])
            del opens[0]
            for m in [[0,1],[1,0],[0,-1],[-1,0]]:
                if not cX+m[1] == -1 and not cY+m[0] == -1:
                    try: 
                            if not [cX+m[1],cY+m[0]] in opens and not [cX+m[1],cY+m[0]] in closes and  not int(lines[cX+m[1]][cY+m[0]])==  9:
                                opens.append([cX+m[1],cY+m[0]])
                    except IndexError:
                        a = 0
        pools.append(len(closes))
    


    pools = sorted(pools) 
 
    return pools[len(pools)-1]*pools[len(pools)-2]*pools[len(pools)-3]


lines = Read_all()
lows, ans1 = Part1(lines)

print("part 1: ", ans1)
print("part 2: ",Part2(lines,lows)) #930412, 128674 rossz!
