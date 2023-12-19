steps = open('151.txt').read().strip().split(',')

def hash(s):
    value = 0
    for c in s:
        value += ord(c)
        value = value * 17 % 256

    return value

print(sum(hash(x) for x in steps))
print(hash('rn'))

boxes = [[] for _ in range(256)]
map = {}

for instruction in steps:
    if '-' in instruction:
        label = instruction[:-1]
        index = hash(label)
        if label in boxes[index]:
            boxes[index].remove(label)
    else:
        label, length = instruction.split('=')
        length = int(length)
        index = hash(label)

        if label not in boxes[index]:
            boxes[index].append(label)

        print(map)

        map[label] = length
        print(map)

total = 0

for b, box in enumerate(boxes, 1):
    for lens_slot, label in enumerate(box, 1):
        total += b * lens_slot * map[label]

print(total)
print(map)
