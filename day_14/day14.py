grid = open('day141.txt').read().splitlines()
# transpose 
grid = list(map(''.join, zip(*grid)))
print(grid)
# transpose again
grid = ["#".join(["".join(sorted(list(group), reverse=True)) for group in row.split("#")]) for row in grid]


print(grid)