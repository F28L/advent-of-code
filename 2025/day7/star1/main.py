import sys

def print_board(board: list[str]) -> None:
    for line in board:
        print(line)


def run():
    print('Reading input...')
    board = sys.stdin.read().strip().split("\n")
    # print_board(board)
    queue = set()
    for i in range(len(board)):
        line = board[i]
        for j in range(len(line)):
            char = board[i][j]
            if char == "S":
                print('Found start of tachyon beam...')
                queue.add((i,j))
    max_rows = len(board)
    max_cols = len(board[0])
    splits = 0
    seen = set()
    while len(queue) > 0:
        # process the current location
        # if the current location is a splitter, add the 2 new locations to the queue and increase the count of splitter
        # if a location is already in the queue, dont add it
        # if the its not, then just add the location directly below it
        curr = queue.pop()
        seen.add(curr)
        r, c = curr[0], curr[1]
        if board[r][c] == "^":
            splits+=1
            print(f"Found a splitter at {r}, {c}...")
            new_r = (r, c+1)
            new_l = (r, c-1)
            if c+1 < max_cols:
                if new_r not in seen:
                    print(f"Adding {new_r} to the queue...")
                    queue.add(new_r)
            if c-1 >= 0:
                if new_l not in seen:
                    print(f"Adding {new_l} to the queue...")
                    queue.add(new_l)
        else:
            if r+1 < max_rows:
                new = (r+1, c)
                if new not in seen:
                    print(f"Adding {new} to the queue...")
                    queue.add(new)
    
    return splits




if __name__ == "__main__":
    print(run())
