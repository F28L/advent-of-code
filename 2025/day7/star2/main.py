import sys

def run():
    board = sys.stdin.read().strip().split("\n")
    max_rows = len(board)
    max_cols = len(board[0])

    paths = [[0]*max_cols for _ in range(max_rows)]

    for c in range(max_cols):
        if board[0][c] == "S":
            paths[0][c] = 1
            break

    for r in range(max_rows-1):
        for c in range(max_cols):
            count = paths[r][c]
            if count == 0:
                continue

            below = board[r+1][c]

            if below == "^":
                if c-1 >= 0:
                    paths[r+1][c-1] += count
                if c+1 < max_cols:
                    paths[r+1][c+1] += count
            else:
                paths[r+1][c] += count

    return paths

if __name__ == "__main__":
    p = run()
    print(sum(p[-1]))
