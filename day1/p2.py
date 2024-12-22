from collections import Counter

INPUT = "day1/.input"
# INPUT = 'day1/example.input'


def load_input():
    ls = []
    rs = []
    with open(INPUT) as f:
        for line in f:
            l, r = map(int, line.split())
            ls.append(l)
            rs.append(r)
    return ls, rs


def main():
    res = 0
    ls, rs = load_input()
    rs_cnt = Counter(rs)
    for l in ls:
        res += l * rs_cnt.get(l, 0)
    print(res)


if __name__ == "__main__":
    main()
