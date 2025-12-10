# puzzle_input = get_dummy_input()
import sys
puzzle_input = sys.stdin.read().strip()
raw_points = puzzle_input.split("\n")

x_vals = []
y_vals = []
for point in raw_points:
    coords = point.split(',')
    x_vals.append(int(coords[0]))
    y_vals.append(int(coords[1]))

# To work with the massive coordinate system this rescales the points.
# Every point is at most a distance of 1 from each other.
unique_x = sorted(set(x_vals))
unique_y = sorted(set(y_vals))
x_map = {x: i for i, x in enumerate(unique_x)}
y_map = {y: i for i, y in enumerate(unique_y)}
compressed_points = [(x_map[x], y_map[y]) for x, y in zip(x_vals, y_vals)]
compressed_set = set(compressed_points)

grid = []
for y in range(len(y_map)):
    row = []
    for x in range(len(x_map)):
        if (x, y) in compressed_set:
            row.append('#')
        else:
            row.append('.')
    grid.append(row)

# This fills in the edges
for i in range(len(compressed_points)):
    x1, y1 = compressed_points[i]
    x2, y2 = compressed_points[(i + 1) % len(compressed_points)]

    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            grid[y1][x] = '#'

    elif x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            grid[y][x1] = '#'

# We can floodfill the EXTERIOR of the polygon to mark is as invalid
OFFSETS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
WIDTH = len(grid[0])
HEIGHT = len(grid)

tracked = set()
to_paint = []

for x in range(WIDTH):
    if grid[0][x] != '#':
        to_paint.append((x, 0))
    if grid[HEIGHT - 1][x] != '#':
        to_paint.append((x, HEIGHT - 1))
    tracked.add((x, 0))
    tracked.add((x, HEIGHT - 1))

for y in range(1, HEIGHT - 1):  # Already included the corners in first loop
    if grid[y][0] != '#':
        to_paint.append((0, y))
    if grid[y][WIDTH - 1] != '#':
        to_paint.append((WIDTH - 1, y))
    tracked.add((0, y))
    tracked.add((WIDTH - 1, y))

while to_paint:
    x, y = to_paint.pop()
    grid[y][x] = 'X'
    for dx, dy in OFFSETS:
        nx = min(max(x + dx, 0), WIDTH - 1)
        ny = min(max(y + dy, 0), HEIGHT - 1)
        if (nx, ny) in tracked or grid[ny][nx] == '#':
            continue
        tracked.add((nx, ny))
        to_paint.append((nx, ny))

# Would take a while to bruteforce every rectangle. Use DP to remember how many Xs are in a region
prefix = [[0] * (WIDTH + 1) for _ in range(HEIGHT + 1)]
for y in range(HEIGHT):
    for x in range(WIDTH):
        prefix[y + 1][x + 1] = prefix[y][x + 1] + prefix[y + 1][x] - prefix[y][x]
        if grid[y][x] == 'X':
            prefix[y + 1][x + 1] += 1

res = 0
for i in range(len(compressed_points)):
    for j in range(i + 1, len(compressed_points)):
        x1, y1 = x_vals[i], y_vals[i]
        x2, y2 = x_vals[j], y_vals[j]
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)
        area = (max_x - min_x + 1) * (max_y - min_y + 1)

        cy1, cy2 = y_map[min_y], y_map[max_y]
        cx1, cx2 = x_map[min_x], x_map[max_x]

        x_count = (prefix[cy2 + 1][cx2 + 1] - prefix[cy1][cx2 + 1]
                   - prefix[cy2 + 1][cx1] + prefix[cy1][cx1])

        if x_count == 0:
            res = max(res, area)

print(res)