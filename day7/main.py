def Read_all():
    with open("input.txt") as f:
        nums=  f.readline().split(',')
    return [int(i) for i in nums]

def Part1(nums):
    min_fuels = 100000000000
    for i in range(min(nums),max(nums)):
        sv=0
        for x in nums:
            sv+=abs(i-x)
        if sv < min_fuels:
            min_fuels = sv 
    return min_fuels
def Part2(nums):
    min_fuels = 100000000000
    for i in range(0,max(nums)):
        step = 0
        for x in nums:
            step += (1+abs(i-x)) * abs(i-x) //2
        if step < min_fuels:
            min_fuels = step 
    return min_fuels
nums = Read_all()
print("part 1: ",Part1(nums))
print("part 2: ", Part2(nums))