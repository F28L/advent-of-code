import sys


def parse_input() -> list[list]:
    grid = []
    for line in sys.stdin:
        grid.append([1 if c == '@' else 0 for c in line.strip()])
    return grid


def print_grid(grid: list[list]):
    for row in grid:
        print(''.join(['@' if c == 1 else '.' for c in row]))


def count_adjacent_rolls(r: int, c: int, grid: list[list]) -> int:
    ct = 0
    rows = len(grid)
    cols = len(grid[0])
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    to_check = []
    for d in directions:
        if 0 <= r + d[0] < rows and 0 <= c + d[1] < cols:
            to_check.append(grid[r + d[0]][c + d[1]])
    ct = sum(to_check)
    print(f'At ({r},{c}) found {ct} adjacent rolls.')
    return ct


def run():
    grid: list[list] = parse_input()
    # print_grid(grid)
    rows = len(grid)
    cols = len(grid[0])
    accessible_rolls = 0
    removed = -1
    while removed != 0:
        removed = 0
        to_update = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    ct = count_adjacent_rolls(r, c, grid)
                    if ct < 4:
                        removed += 1
                        to_update.append((r, c))

        for u in to_update:
            grid[u[0]][u[1]] = 0
        accessible_rolls += removed
        print(f'Removed {removed} rolls this iteration.')

    return accessible_rolls


if __name__ == "__main__":
    print(run())
