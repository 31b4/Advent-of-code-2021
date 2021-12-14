from collections import  defaultdict
with open("input.txt") as f:
    key,lines = f.read().split("\n\n")
    lines = [x.split(" -> ") for x in lines.splitlines()]
twins = defaultdict(int)
digits = defaultdict(int)
for char in key:
    digits[char]+=1
for x in range(len(key)-1):
    twins[key[x:x+2]]+=1

print(twins)
for i in range(40):
    for check,ins in lines:
        if twins[check] >0:
            digits[ins] +=twins[check]
            twins[check[0]+ins] += twins[check]
            twins[ins+check[1]] += twins[check]
            del twins[check]


# for i in range(10):

#     new = key
#     for check,ins in lines:
#         for x in range(len(key)-1):
#             if check in key[x:x+2]:
#                 new = new[:new.index(check)+1] +ins+new[new.index(check)+1:]
#                 digits[ins] +=1
#     key = new

print(digits)
print(max(digits.values()) - min(digits.values()))


#nem jo: 1680996794131622572779692