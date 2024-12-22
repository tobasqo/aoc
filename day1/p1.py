import heapq

heappop = heapq.heappop

INPUT = 'day1/.input'
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
    heapq.heapify(ls)
    heapq.heapify(rs)
    while ls and rs:
        l = heappop(ls)
        r = heappop(rs)
        res += abs(l - r)
    print(res)


if __name__ == "__main__":
    main()
