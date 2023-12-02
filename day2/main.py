import time
import re

RED = 12
GREEN = 13
BLUE = 14


def get_sets(input):
    pattern = re.compile(r'(\d+)\s+(\w+)')
    return re.findall(pattern, input)


def calculate_power(matches):
    max_values = {"red": 0, "green": 0, "blue": 0}

    for value, color in matches:
        value = int(value)
        if value > max_values[color]:
            max_values[color] = value

    return max_values["red"] * max_values["green"] * max_values["blue"]


def valid_games(matches):
    is_valid = all(entry[1] != color or int(entry[0]) <= threshold for threshold, color in
                   [(BLUE, 'blue'), (RED, 'red'), (GREEN, 'green')] for entry in matches)

    return is_valid


def part1(input_text):
    start_time = time.time()
    game_ids = []
    with open(input_text) as file:
        for index, line in enumerate(file):
            line_split = line.split("Game ")
            cubes = line_split[1].split(": ")[1]
            matches = get_sets(cubes)
            valid_games(matches) and game_ids.append(index+1)

    print(f"Result part1: {sum(game_ids)} with a time of {time.time() - start_time}")


def part2(input_text):
    start_time = time.time()
    minimum_power = []
    with open(input_text) as file:
        for line in file:
            line_split = line.split("Game ")
            cubes = line_split[1].split(": ")[1]
            matches = get_sets(cubes)
            minimum_power.append(calculate_power(matches))

    print(f"Result part2: {sum(minimum_power)} with a time of {time.time() - start_time}")


part1("input.txt")
part2("input.txt")
