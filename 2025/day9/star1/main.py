import sys

def run():
    coords = []
    for line in sys.stdin:
        x, y = map(int, line.strip().split(","))
        coords.append((x, y))
    max_area = -1
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            (x1, y1), (x2, y2) = coords[i], coords[j]
            area = abs(x1 - x2 + 1) * abs(y1 - y2 + 1)
            if area > max_area:
                print(f'New max area {area} found with points ',
                      f'({x1},{y1}) and ({x2},{y2}).')
                max_area = area
    return max_area

if __name__ == "__main__":
    result = run()
    print(result)