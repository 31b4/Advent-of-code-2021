def Read_all():
    with open("input.txt") as f:
        nums=  f.readline().split(',')
    return [int(i) for i in nums]

def Part1(line):
    for i in range(80):
        print(i)
        for x in range(len(line)):
            if line[x]==0:
                line[x]=6
                line.append(8)
            else:
                line[x] -=1
    return line
def Part2(nums):
    pass
nums = Read_all()
print(len(Part1(nums)))
print(len(Part1(nums,256)))
