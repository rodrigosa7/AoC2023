import re
import time


def main():
    start_time = time.time()
    stars = []
    with open("input.txt") as file:
        for line in file:
            not_numbers = re.sub("[^0-9]", "", line)
            stars.append(int(not_numbers[0] + not_numbers[-1]))

    print(sum(stars))
    print("%s seconds to execute" % (time.time() - start_time))


main()
