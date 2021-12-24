with open('input.txt') as f:
    lines = f.readlines()
for i in range(len(lines)):
    line = lines[i].split('\n')
    lines[i] = line[0]
gamma_rate = ""
for j in range(len(lines[0])):
    line = []
    for i in range(len(lines)):
        line.append(int(lines[i][j]))
    asd = str((max(set(line), key = line.count)))
    gamma_rate+=asd
epsilon_rate = ""
for i in range(len(gamma_rate)):
    if gamma_rate[i] == "1":
        epsilon_rate+="0"
    else:
        epsilon_rate+="1"

print("part 1: ",int(gamma_rate,2)*int(epsilon_rate,2))
nums = lines
pos = 0
while len(nums)>1:
    line = []
    vip_nums = []
    zero = 0
    one = 0
    most_used = 0
    for i in range(len(nums)):
        line.append(int(nums[i][pos]))
    for num in line:
        if num == 1:
            one +=1
        else:
            zero+=1
    if one >=zero:
        most_used = "1"
    elif zero>one:
        most_used ="0"
    for item in nums:
        if item[pos] == most_used:
            vip_nums.append(item)
    nums = vip_nums
    pos+=1
nums2 = lines
pos2 = 0
while len(nums2)>1:
    line = []
    vip_nums = []
    zero = 0
    one = 0
    less_used = 0
    for i in range(len(nums2)):
        line.append(int(nums2[i][pos2]))
    for num in line:
        if num == 1:
            one +=1
        else:
            zero+=1
    if zero<=one:
        less_used ="0"
    elif one <zero:
        less_used = "1"
    for item in nums2:
        if item[pos2] == less_used:
            vip_nums.append(item)
    nums2 = vip_nums
    pos2+=1
if len(nums)==1:
    nums = str(nums[0])
if len(nums2)==1:
    nums2 = str(nums2[0])


print("part 2: ", int(nums,2)*int(nums2,2))
