import sys


def run():
    print('Reading input...')
    grid = []
    for line in sys.stdin:
        elements = []
        to_process = line.strip().split(' ')
        for x in to_process:
            if len(x) > 0:
                elements.append(x)
        grid.append(elements)
    print(grid)
    print('Finished reading input...')
    count = 0
    for c in range(len(grid[0])):
        operation = grid[-1][c]
        to_operate = [int(grid[x][c]) for x in range(len(grid)-1)]
        print(operation, to_operate)
        if operation == '*':
            product = 1
            for i in range(len(to_operate)):
                product *= to_operate[i]
            print(f'Column {c} has value {product}.')
            count += product
        else:
            s = sum(to_operate)
            print(f'Column {c} has value {s}.')
            count+=s
    return count



if __name__ == "__main__":
    print(run())
