with open('input.txt') as f:
    lines = f.readlines()

counter = 0
for i in range(1,len(lines)):
    if int(lines[i])>int(lines[i-1]):
        counter+=1
print("part 1: ",counter)


counter2 =0
for i in range(3,len(lines)):
    if int(lines[i-2])+int(lines[i-1])+int(lines[i]) > int(lines[i-3])+int(lines[i-2])+int(lines[i-1]):
        counter2+=1
print("part 2: ",counter2)
