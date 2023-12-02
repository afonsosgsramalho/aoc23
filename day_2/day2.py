import re
from collections import defaultdict
import math

def process_data():
    with open("day2.txt") as f:
        ls = f.read().strip().split("\n")

    return ls


def part_one_two(data):
    ids = 0
    powers = 0
    for l in data:
        parts = re.sub("[;,:]", "", l).split()
        colormax = defaultdict(int)
        for count, color in zip(parts[2::2], parts[3::2]):
            colormax[color] = max(colormax[color], int(count))
        powers += colormax['red'] * colormax['green'] * colormax['blue']
        if colormax['red'] <= 12 and colormax['green'] <= 13 and colormax['blue'] <= 14:
            ids += int(parts[1])

    return ids, powers

    
def main():
    data = process_data()
    part_one, part_two = part_one_two(data)
    print(part_one)
    print(part_two)


if __name__ == '__main__':
    main()


