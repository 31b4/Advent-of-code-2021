def Read_all():
    with open("input.txt") as f:
        return f.read().split('\n')

def Solution(lines):
    chars = {
        "(": ")",
        "<": ">",
        "[": "]",
        "{": "}",
    }
    points = {
        ")": 3,
        ">": 25137,
        "]": 57,
        "}": 1197,
    }
    summ = 0
    incomplete = []
    for line in lines:
        stack = []
        valid = False
        for word in line:
            if word in chars:
                stack.append(chars[word])
            elif word == stack.pop():
                pass
            else:
                summ += points[word]
                valid = True
                break
        if not valid and len(stack)>0:
            incomplete.append(stack)
    print("part 1: ",summ)
    part2points = {
        ")": 1,
        ">": 4,
        "]": 2,
        "}": 3,
    }
    part2 = []
    for x in incomplete:
        sv = 0
        while x:
            sv = sv*5 + part2points[x.pop()]
        part2+= [sv]
    part2.sort()
    print("part 2: ",part2[int(len(part2)/2)])
lines = Read_all()
Solution(lines)


