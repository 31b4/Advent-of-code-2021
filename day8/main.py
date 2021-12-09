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
def Part2(lines):
    for x in lines:
        summ = 0
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
            elif len(item) == 5:
                pass
            elif len(item) == 6:
                pass
        for item in first.split(' '):
            if len(item) == 5:
                three = True
                for x in nums[1]:#3 check
                    if x not in item:
                        three = True
                if three:
                    nums[3] = item
                five = True
                missing = 0
                for x in nums[6]:#5 check
                    if x not in item:
                        missing +=1
                five = missing == 1
                if five and not three:
                    nums[5] = item
                if not five and not three:
                    nums[2] = item

        for item in first.split(' '):
            sorted_char = sorted(item)
            item = "".join(sorted_char)
            if len(item) == 6:
                nine = False
                for x in nums[4]:#9 check
                    if x not in item:
                        nums[9] = item
                        nine = True
                zero = False
                if not nine:
                    for x in nums[4]:#0 check
                        if x not in item:
                            nums[0] = item
                            zero = True
                if not nine and not zero:
                    nums[6] = item
    #     print(nums)
    #     num = 0
    #     for find in second.split(' '):
    #         for i in range(10):
    #             if nums[i] == find:
    #                 num = (num *10) +i
    #     summ += num
    # return summ



lines = Read_all()
print("part 1: ", Part1(lines))
print("part 2: ", Part2(lines))
