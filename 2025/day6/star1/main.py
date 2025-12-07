import sys


def run():
    print('Reading input...')
    txt = sys.stdin.read().strip()
    ranges, ids = txt.split('\n\n')
    print('Finished reading input...')
    print('Defining fresh id ranges...')
    fresh_ids = []
    for r in ranges.strip().split('\n'):
        s = r.split('-')
        left = int(s[0])
        right = int(s[1])
        fresh_ids.append((left, right))
    print('Finished defining fresh ids')
    print(fresh_ids)
    ct_fresh = 0
    print('Processing ids...')
    for line in ids.strip().split('\n'):
        id = int(line)
        for r in fresh_ids:
            if r[0] <= id <= r[1]:
                ct_fresh += 1
                print(f'Found fresh id: {id}')
                break
    return ct_fresh


if __name__ == "__main__":
    print(run())
