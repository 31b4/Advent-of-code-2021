with open("input.txt", "r") as file:
    nums = list(map(int, file.read().split(",")))
print(nums)
# memoized recursion
memory = {}
def children_after(n):
    if n < 0: return 0
    if n not in memory: memory[n] = 1 + children_after(n-7) + children_after(n-9)
    return memory[n]

print(sum(children_after(79-k) for k in nums) + len(nums)) # part 1
print(sum(children_after(255-k) for k in nums) + len(nums)) # part 2