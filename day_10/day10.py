from collections import deque

grid = open('day10.txt').read().strip().splitlines()

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.


for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == 'S':
            sr = r
            sc = c
            break
    else:
        continue
    break

seen = {(sr, sc)}
q = deque([(sr, sc)])

maybe_s = {"|", "-", "J", "L", "7", "F"}

while q:
    r, c = q.popleft()
    ch = grid[r][c]

    # check up
    if r > 0 and ch in 'S|JL' and grid[r - 1][c] in '|7F' and (r - 1, c) not in seen:
        seen.add((r - 1, c))
        q.append((r - 1, c))
        if ch == "S":
            maybe_s &= {"|", "J", "L"}
    # check down
    if r < len(grid) - 1 and ch in 'S|7F' and grid[r + 1][c] in '|JL' and (r + 1, c) not in seen:
        seen.add((r + 1, c))
        q.append((r + 1, c))
        if ch == "S":
            maybe_s &= {"|", "7", "F"}
    # check right
    if c > 0 and ch in 'S-J7' and grid[r][c - 1] in '-LF' and (r, c - 1) not in seen:
        seen.add((r, c - 1))
        q.append((r, c - 1))
        if ch == "S":
            maybe_s &= {"-", "J", "7"}
    # check left 
    if c < len(grid[r]) - 1 and ch in 'S-LF' and grid[r][c + 1] in '-7J' and (r, c + 1) not in seen:
        seen.add((r, c + 1))
        q.append((r, c + 1))
        if ch == "S":
            maybe_s &= {"-", "L", "F"}

assert len(maybe_s) == 1
(S,) = maybe_s

grid = [row.replace('S', S) for row in grid]
grid = [''.join(ch if (r, c) in seen else '.' for c, ch in enumerate(row)) for r, row in enumerate(grid)]

print(grid)

outside = set()

for r, row in enumerate(grid):
    within = False
    up = None
    for c, ch in enumerate(row):
        if ch == "|":
            assert up is None
            within = not within
        elif ch == "-":
            assert up is not None
        elif ch in "LF":
            assert up is None
            up = ch == "L"
        elif ch in "7J":
            assert up is not None
            if ch != ("J" if up else "7"):
                within = not within
            up = None
        elif ch == ".":
            pass
        else:
            raise RuntimeError(f"unexpected character (horizontal): {ch}")
        if not within:
            outside.add((r, c))

print(len(grid) // 2)
print(len(grid) * len(grid[0]) - len(outside | seen))

