# INPUT = "day4/.input"
INPUT = "day4/example2.input"


def load_input():
    with open(INPUT) as f:
        return f.read().splitlines()


def in_bounds(x: int, max_x: int, y: int, max_y: int):
    return 0 <= x < max_x and 0 <= y < max_y


def create_diagonals(input: list[str], x: int, y: int):
    return (
        input[x - 1][y - 1] + input[x][y] + input[x + 1][y + 1],
        input[x - 1][y + 1] + input[x][y] + input[x + 1][y - 1],
    )


def main():
    res = 0
    input = load_input()
    m = len(input)
    n = len(input[0])
    for row in range(m):
        for col in range(n):
            if input[row][col] != "A":
                continue

            if not all(
                [
                    in_bounds(row - 1, m, col - 1, n),
                    in_bounds(row - 1, m, col + 1, n),
                    in_bounds(row + 1, m, col - 1, n),
                    in_bounds(row + 1, m, col + 1, n),
                ]
            ):
                continue

            diags = create_diagonals(input, row, col)
            if all(diag in ("MAS", "SAM") for diag in diags):
                res += 1
    print(res)


if __name__ == "__main__":
    main()
