import sys
# this is broken i need to fix it

def print_grid(grid):
    for row in grid:
        print("".join(str(cell) for cell in row))
    print('\n')


def run():
    coords = []
    max_x, max_y = 0, 0
    for line in sys.stdin:
        x, y = map(int, line.strip().split(","))
        coords.append((x, y))
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    grid = [['*' for _ in range(max_x+1)] for _ in range(max_y+1)]
    max_area = -1
    print_grid(grid)
    for coord in coords:
        grid[coord[1]][coord[0]] = "#"
    print_grid(grid)
    i = len(coords)-1
    j = len(coords)-2
    while i >= 0 and j >= -1:
        (x1, y1), (x2, y2) = coords[i], coords[j]
        if x1 == x2:
            # draw a vertical line
            print(f'Drawing vertical line between ({x1},{y1}) and ({x2},{y2})')
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if grid[y][x1] == '*':
                    grid[y][x1] = 'X'
        elif y1 == y2:
            # draw a horizontal line
            print(f'Drawing horizontal line between ({x1},{y1}) and ({x2},{y2})')
            for x in range(min(x1, x2), max(x1, x2) + 1):
                if grid[y1][x] == '*':
                    grid[y1][x] = 'X'
        j -= 1
        i -= 1

    print_grid(grid)
    # how do i fill in the fenced off area???
    for i in range(len(grid)):
        inside = False
        for j in range(len(grid[0])):
            if grid[i][j] in ('#', 'X'):
                inside = True
            elif inside:
                grid[i][j] = 'I'

    print_grid(grid)
    for i in range(len(coords)):
        for j in range(i+1, len(coords)):
            (x1, y1), (x2, y2) = coords[i], coords[j]
            if x1 != x2 and y1 != y2:
                print(f'Checking rectangle corners: ({x1},{y1}), ({x2},{y2}), ({x1},{y2}), ({x2},{y1})')
                area = 0
                # tmp_grid = grid
                # tmp_grid[y1][x2] = '0'
                # tmp_grid[y2][x1] = '0'
                # tmp_grid[y1][x1] = '0'
                # tmp_grid[y2][x2] = '0'
                # print_grid(tmp_grid)
                for m in range(min(y1, y2), max(y1, y2) + 1):
                    for n in range(min(x1, x2), max(x1, x2) + 1):
                        if grid[m][n] not in ('#', 'X'):
                            print(f'Invalid area due to cell ({n},{m}) = {grid[m][n]}')
                            area = -1
                            break
                        else:
                            area += 1
                    if area == -1:
                        break
                if area > max_area:
                    max_area = area
                    print(f'New max area found: {max_area} with corners ({x1},{y1}), ({x2},{y2})')

    # for each red corner, find all other possible red corners within the fenced off area
        # a candidate red corner must have either a smaller x and smaller y, or larger x and larger y
        # then if the area is valid, all components within the area must be either '*' or 'X'
    # Compute area of the sub area
    # If area larger, then update max
    return max_area



if __name__ == "__main__":
    result = run()
    print(result)