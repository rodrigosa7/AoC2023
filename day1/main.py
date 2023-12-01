import re
import time


def part1(line_file):
    start_time = time.time()
    stars = []
    with open(line_file) as file:
        for line in file:
            only_numbers = re.sub("[^0-9]", "", line)
            stars.append(int(only_numbers[0] + only_numbers[-1]))

    print("Result part 1: %d" % sum(stars))
    print("%s seconds to execute" % (time.time() - start_time))


def get_numbers(line: str):
    numbers_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    numbers = []
    while line != "":
        if line[0].isnumeric():
            numbers.append(line[0])
            line = line[1:]
        else:
            for element in numbers_dict.keys():
                if line.startswith(element):
                    numbers.append(numbers_dict[element])
            line = line[1:]

    return numbers


def part2(line_file):
    start_time = time.time()
    stars = []

    with open(line_file) as file:
        for line in file:
            numbers = get_numbers(line)
            stars.append(int(numbers[0] + numbers[-1]))

    print("Result part 2: %d" % sum(stars))

    print("%s seconds to execute" % (time.time() - start_time))


def main():
    print("Day 1 Part 1 execution")
    part1("input.txt")
    print("Day 1 Part 2 execution")
    part2("input.txt")


main()
