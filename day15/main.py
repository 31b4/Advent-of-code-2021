def ReadAll():
    nums = []
    with open('input.txt', 'r') as file:
        for i, line in enumerate(file):
            line = line.strip('\n')
            nums.append([int(num) for num in line])
        return nums
def Solve(solved):
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            upper = -1
            left = -1
            if i > 0:
                upper=(solved[i-1][j])
            if j > 0:
                left=(solved[i][j-1])
            if upper == -1 and left == -1:
                solved[i][j] = 0
            elif upper == -1 and left != -1:
                solved[i][j] = nums[i][j] + left
            elif upper != -1 and left == -1:
                solved[i][j] = nums[i][j] + upper
            elif upper<=left:
                solved[i][j] = nums[i][j]+upper
            elif left <upper:
                solved[i][j] = nums[i][j]+left
    return solved[len(solved)-1][len(solved[0])-1]
def make25times(matrix):
    bigmatrix = matrix
    for i in range(len(matrix)):#horizontalis
        for j in range(len(matrix[i])*4):
            if bigmatrix[i][j]+1 > 9:
                bigmatrix[i].append(1)
            else:
                bigmatrix[i].append(bigmatrix[i][j]+1)
    for i in range(len(bigmatrix)*4):#vertikalis
        line = []
        for j in range(len(matrix[i])):
            if bigmatrix[i][j]+1 > 9:
                line.append(1)
            else:
                line.append(bigmatrix[i][j]+1)
        bigmatrix.append(line)
    return bigmatrix
nums = ReadAll()
print("part 1: ",Solve(nums))
nums = ReadAll()
print("part 2: ",Solve(make25times(nums)))
