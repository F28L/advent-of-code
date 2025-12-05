import sys


def run():
    print('Reading input...')
    input = sys.stdin.read().strip()
    ranges, ids = input.split('\n\n')
    print('Finished reading input...')
    print('Defining fresh ids...')
    fresh_ids = set()
    for r in ranges.strip().split('\n'):
        print('Processing range:', r)
        left, right = r.split('-')
        new = {i for i in range(int(left), int(right)+1)}
        fresh_ids = fresh_ids.union(new)
    # print(fresh_ids)
    print('Finished defining fresh ids')
    print(fresh_ids)
    ct_fresh = 0
    print('Processing ids...')
    for line in ids.strip().split('\n'):
        id = int(line)
        if id in fresh_ids:
            ct_fresh += 1
    return ct_fresh


if __name__ == "__main__":
    print(run())
