INPUT = "day4/.input"


# INPUT = "day4/example.input"


def load_input():
    with open(INPUT) as f:
        return f.read().splitlines()


def gen_directions():
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            yield dx, dy


def in_bounds(x: int, max_x: int, y: int, max_y: int):
    return 0 <= x < max_x and 0 <= y < max_y


def main():
    res = 0
    input = load_input()
    m = len(input)
    n = len(input[0])
    for row in range(m):
        for col in range(n):
            for dx, dy in gen_directions():
                no_errors = True
                for i, c in enumerate("XMAS"):
                    row_delta = row + i * dx
                    col_delta = col + i * dy
                    if not in_bounds(row_delta, m, col_delta, n):
                        no_errors = False
                        break
                    if input[row_delta][col_delta] != c:
                        no_errors = False
                        break
                if no_errors:
                    res += 1
    print(res)


if __name__ == "__main__":
    main()
