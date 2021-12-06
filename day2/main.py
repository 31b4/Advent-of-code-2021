from os import spawnl


with open('input.txt') as f:
    lines = f.readlines()
horizontal =0
depth = 0
for line in lines:
    word = line.split(' ')
    if word[0]== "forward":
        horizontal+=int(word[1])
    elif word[0] == "down":
        depth +=int(word[1])
    elif word[0] == "up":
        depth-=int(word[1])

print(horizontal*depth)
horizontal = 0
depth=0
aim = 0
for line in lines:
    word = line.split(' ')
    if word[0]== "forward":
        horizontal+=int(word[1])
        depth += aim*int(word[1])
    elif word[0] == "down":
        aim +=int(word[1])
    elif word[0] == "up":
        aim -=int(word[1])
print(horizontal*depth)

