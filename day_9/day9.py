lines = open('day9.txt').read().split('\n')

def get_diff(nums):

    if all(x == 0 for x in nums):
        return 0
    deltas = []
    for i in range(1, len(nums)):
        deltas.append(nums[i] - nums[i - 1])
    # deltas = [y - x for x, y in zip(nums, nums[1:])] other way to do it
    diff = get_diff(deltas)

    return nums[-1] + diff # part1
    # return nums[0] - diff # part2

total = 0
for line in lines:
    nums = list(map(int, line.split()))
    total += get_diff(nums)

print(total)


