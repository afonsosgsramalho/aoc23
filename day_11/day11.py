lines = open('day11.txt').read().splitlines()

# # add rows
# matrix = []
# for l, line in enumerate(lines):
#     matrix.append(line)
#     if all(x == '.' for x in line):
#         matrix.append(line)
# # transpose and add columns
# matrix_t = []
# for line in zip(*matrix):
#     matrix_t.append(''.join(x for x in line))
#     if all(x == '.' for x in line):
#         matrix_t.append(''.join(x for x in line))
# # transpose again and create final matrix
# final_matrix = [''.join(x for x in line) for line in zip(*matrix_t)]
# print(''.join(x + '\n' for x in final_matrix))

empty_rows = [r for r, row in enumerate(lines) if all(ch == '.' for ch in row)]
empty_cols = [c for c, col in enumerate(zip(*lines)) if all(ch == '.' for ch in col)]

total = 0
scale = 1000000

points = [(r, c) for r, row in enumerate(lines) for c, col in enumerate(row) if col == '#']

for i, (r1, c1) in enumerate(points):
    for (r2, c2) in points[i:]:
        for r in range(min(r1, r2), max(r1, r2)):
            total += scale if r in empty_rows else 1
        for c in range(min(c1, c2), max(c1, c2)):
            total += scale if c in empty_cols else 1

print(total)


