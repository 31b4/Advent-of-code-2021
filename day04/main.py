def Read_all():
    with open("input.txt") as f:
        raw = f.read().strip()
        lines = raw.split("\n")
        return lines

def Convert_readable(lines):
    numbers = list(map(int, lines[0].split(",")))
    data=[]
    for line in lines[1:]:
        sv = []
        for num in line.split(' '):
            sv2 = [0,0]
            if num != "":
                sv2[0] = int(num)
                sv.append(sv2)
        if len(sv) == 5:
            data.append(sv)
    return data,numbers

def Check_winner(data,j,k):
    winner = True
    for i in range(len(data[j])): #lines
        if data[j][i][1]==0:
            winner = False
            break
    if winner:
        return True
    for i in range((int(j/5)*5),(int(j/5)*5)+5):
        if data[i][k][1] == 0:
            return False
    return True
    
def Nulls_of_board(data,index):
    summ = 0
    for i in range((int(index/5)*5),(int(index/5)*5)+5):
        for j in range(5):
            if data[i][j][1] == 0:
                summ+= data[i][j][0]
    return summ
def Part1(numbers,data):
    for num in numbers:
        for j in range(len(data)):
            for i in range(len(data[j])):
                if data[j][i][0] == num:
                    data[j][i][1] = 1
                    if Check_winner(data,j,i):
                        return data[j][i][0]*Nulls_of_board(data,j)
def Part2(numbers,data):
    for num in numbers:
        for j in range(len(data)):
            for i in range(len(data[j])):
                if data[j][i][0] == num:
                    data[j][i][1] = 1
                    if Check_winner(data,j,i)and len(data)>5:
                        del data[int(j/5)*5:int(j/5)*5+5]
                        return False,data
                    elif Check_winner(data,j,i)and len(data)==5:
                        return True,data[j][i][0]*Nulls_of_board(data,j)
data,numbers = Convert_readable(Read_all())
print("part 1: ",Part1(numbers,data))
found,data = Part2(numbers,data)
while not found:
    found,data= Part2(numbers,data)
print("part 2: ",data)
