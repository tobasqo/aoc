INPUT = 'day2/.input'
# INPUT = 'day2/example.input'


def load_input():
    with open(INPUT) as f:
        for line in f:
            yield tuple(map(int, line.split()))


def is_safely_increasing(report: tuple[int, ...]):
    for i in range(1, len(report)):
        dif = report[i] - report[i-1]
        if dif <= 0 or dif > 3:
            return False
    return True


def is_safely_decreasing(report: tuple[int, ...]):
    for i in range(1, len(report)):
        dif = report[i-1] - report[i]
        if dif <= 0 or dif > 3:
            return False
    return True


def main():
    res = 0
    input = load_input()
    for report in input:
        if is_safely_increasing(report) or is_safely_decreasing(report):
            res += 1
    print(res)


if __name__ == "__main__":
    main()
