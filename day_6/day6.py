def get_input(part):
    with open ('day6.txt') as file:
        if part == 'part1':
            time = list(map(int, file.readline().strip().split('Time:')[1].split()))
            distance = list(map(int, file.readline().strip().split('Distance:')[1].split()))
            return time, distance
        if part == 'part2':
            time = int(''.join(file.readline().strip().split('Time:')[1].split()))
            distance = int(''.join(file.readline().strip().split('Distance:')[1].split()))    
            return time, distance


def part_one(time, distance):
    result_list = list(zip(time, distance))
    result = 1

    for time, distance in result_list:
        holds = 0
        higher = 0

        while holds <= time:
            holds += 1
            if (time - holds) * holds > distance:
                higher += 1

        result *= higher
    
    return result


def part_two(time, distance):
    result = 1
    holds = 0
    higher = 0

    while holds <= time:
        holds += 1
        if (time - holds) * holds > distance:
            higher += 1

    result *= higher
    
    return result

if __name__ == '__main__':
    time1, distance1 = get_input('part1')
    time2, distance2 = get_input('part2')
    
    print(part_one(time1, distance1))
    print(part_two(time2, distance2))