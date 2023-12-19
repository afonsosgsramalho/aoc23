lines = open('day18.txt').read().split('\n')

dirs = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}
dir_exe = {
    '0': 'R',
    '1': 'D',
    '2': 'L',
    '3': 'U'
}

points = [(0, 0)]
points2 = [(0, 0)]
per = 0

for line in lines:
    dir, places, hex = line.split()
    # dir = dir_exe[hex[-2]]        PART TWO
    # places = int(hex[2:-2], 16)   PART TWO
    places = int(places)
    dr, dc = dirs[dir]
    per += places
    r, c = points[-1]
    points.append((r + dr * places, c + dc * places))


def shoelace_area_aux(points):
    area = 0
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        area += (x1 * y2 - x2 * y1)

    area = abs(area) / 2
    final = area + (per / 2) + 1
    
    return final

print(shoelace_area_aux(points))
