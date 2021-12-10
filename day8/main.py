def Read_all():
    with open("input.txt") as f:
        return f.read().split('\n')

def Part1(lines):
    output = 0
    for x in lines:
        check = x.split('| ')[1]
        for y in check.split(' '):
            if len(y) == 2 or len(y) == 3 or len(y) == 4 or len(y) == 7:
                output += 1
    return output


def isNine(lines,item):
    nine = True
    for x in lines[4]:
        if not x  in item:
            nine = False
            break
    return nine
def isZero(lines,item):
    zero = True
    for x in lines[1]:
        if not x  in item:
            zero = False
            break
    return zero
def isThree(lines,item):
    three = True
    for x in lines[1]:
        if not x  in item:
            three = False
            break
    return three
def isFive(lines,item):
    missing = 0
    for x in lines[6]:
        if not x  in item:
            missing+=1
    return missing == 1
def Part2(lines):
    summ = 0
    for x in lines:
        first, second = x.split('| ')
        nums =["","","","","","","","","",""]
        for item in first.split(' '):
            if len(item) == 2:
                nums[1] = item
            elif len(item) == 3:
                nums[7] = item
            elif len(item) == 4:
                nums[4] = item
            elif len(item) == 7:
                nums[8] = item


        for item in first.split(' '):
            if len(item) == 6:
                if isNine(nums,item):
                    nums[9]= item
                elif isZero(nums,item):
                    nums[0] = item
                else:
                    nums[6] = item


        for item in first.split(' '):
            if len(item) == 5:
                if isThree(nums,item):
                    nums[3]= item
                elif isFive(nums,item):
                    nums[5] = item
                else:
                    nums[2] = item
        for i in range(10):
            nums[i] = ''.join(sorted(nums[i]))
        num = 0
        for find in second.split(' '):
            sortedString = ''.join(sorted(find))
            for i in range(10):
                if nums[i] == sortedString:
                    num = (num *10) +i
        print(num)
        summ += num
    return summ



lines = Read_all()
print("part 1: ", Part1(lines))
print("part 2: ", Part2(lines))
