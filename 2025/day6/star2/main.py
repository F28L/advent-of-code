import sys

def run():
    raw = [line.rstrip("\n") for line in sys.stdin]
    grid = [list(row) for row in raw]

    rows = len(grid)
    cols = len(grid[0])

    problems = []
    current = []
    for c in range(cols - 1, -1, -1):
        column = [grid[r][c] for r in range(rows)]
        if all(ch == " " for ch in column):   # separator column
            if current:
                problems.append(current)
                current = []
        else:
            current.append(column)

    if current:
        problems.append(current)

    total = 0

    for problem in problems:
        problem = problem[::-1]

        op = problem[0][-1]

        nums = []
        for col in problem:
            digits = col[:-1]  # all but the operator row
            number_str = "".join(digits).strip()
            nums.append(int(number_str))

        if op == "*":
            acc = 1
            for n in nums:
                acc *= n
        else:
            acc = sum(nums)

        total += acc

    return total


if __name__ == "__main__":
    print(run())
