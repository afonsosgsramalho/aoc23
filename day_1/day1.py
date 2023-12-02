def _replace_words_with_digits(input_string):
    #Because it can be influecing before and after words
    input_string = (
        input_string.replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
    )
    return input_string


def input_aoc(part):
    lines_list1 = open('day1.txt').read().splitlines()
    lines_list2 = []

    for line in lines_list1:
        line_replaced = _replace_words_with_digits(line)
        lines_list2.append(line_replaced)

    if part == 'part1':
        return lines_list1
    if part == 'part2':
        return lines_list2


def part_one(input):
    sum = 0
    cal_values = []
    cal_sum = ''

    for line in input:
        for car in line:
            if car.isdigit():
                cal_values.append(car)

        cal_sum += cal_values[0]
        cal_sum += cal_values[-1]
        sum += int(cal_sum)
        cal_values = []
        cal_sum = ''

    return sum


def part_two(input):
    return part_one(input)


def main():
    lines1 = input_aoc('part1')
    lines2 = input_aoc('part2')

    print(part_one(lines1))
    print(part_two(lines2))


if __name__ == '__main__':
    main()
