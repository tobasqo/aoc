import re

INPUT = 'day3/.input'
# INPUT = 'day3/example1.input'

MUL_PATTERN = re.compile(r'mul\(\d{1,3},\d{1,3}\)')


def load_input():
    with open(INPUT) as f:
        return f.read()


def main():
    res = 0
    input = load_input()
    for match in re.findall(MUL_PATTERN, input):
        a, b = map(int, match[4:-1].split(','))
        res += a * b
    print(res)


if __name__ == '__main__':
    main()
