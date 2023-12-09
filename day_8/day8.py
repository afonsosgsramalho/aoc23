from math import gcd

directions = open('day8.txt').readline().strip()
board = open('day8.txt').read().strip().split('\n')[2:]

board_dict = {}
for b in board:
    board_dict[b.split('=')[0].strip()] = [b.split('=')[1].split(',')[0].strip()[1:], b.split('=')[1].split(',')[1].strip()[:-1]]


def part_one():
    step_count = 0
    letter = 'AAA'

    while letter != 'ZZZ':
        step_count += 1
        letter = board_dict[letter][0 if directions[0] == 'L' else 1]
        directions = directions[1:] + directions[0]
    
    return step_count


def part_two():
    positions = [key for key in board_dict if key.endswith('A')]
    cycles = []

    for current in positions:
        cycle = []

        current_steps = directions
        step_count = 0
        first_z = None
    
        while True:
            while step_count == 0 or not current.endswith('Z'):
                step_count += 1
                current = board_dict[current][0 if current_steps[0] == 'L' else 1]
                current_steps = current_steps[1:] + current_steps[0]

            cycle.append(step_count)

            if first_z is None:
                first_z = current
                step_count = 0
            elif current == first_z:
                break

        cycles.append(cycle)
    print(cycles)

    nums = [cycle[0] for cycle in cycles]
    lcm = nums.pop()

    for num in nums:    
        lcm = lcm * num // gcd(lcm, num)

    return lcm


print(part_two())