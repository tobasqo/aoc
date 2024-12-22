import re

INPUT = "day3/.input"
# INPUT = 'day3/example2.input'

MUL_PATTERN = re.compile(
    r"(?P<mul>mul\(\d{1,3},\d{1,3}\))|(?P<do>do\(\))|(?P<dont>don\'t\(\))"
)


def load_input():
    with open(INPUT) as f:
        return f.read()


def main():
    res = 0
    input = load_input()
    mul_enabled = True
    for match in MUL_PATTERN.finditer(input):
        instruction_name, instruction = next(
            (instruction_name, instruction)
            for (instruction_name, instruction) in match.groupdict().items()
            if instruction
        )
        if instruction_name == "do":
            mul_enabled = True
        elif instruction_name == "dont":
            mul_enabled = False
        elif mul_enabled:
            a, b = map(int, instruction[4:-1].split(","))
            res += a * b
    print(res)


if __name__ == "__main__":
    main()
