import sys


def run():
    print('Reading input...')
    txt = sys.stdin.read().strip()
    ranges, ids = txt.split('\n\n')
    print('Finished reading input...')
    print('Defining fresh id ranges...')
    fresh_ids = []
    for r in ranges.strip().split('\n'):
        print('Processing range:', r)
        left, right = r.split('-')
        i = 0
        while i < len(fresh_ids):
            id_range = fresh_ids[i]
            print('Comparing to range:', id_range)
            if not (int(right) < id_range[0] or int(left) > id_range[1]):
                # Overlap so merge range
                print('Overlaps with existing range, merging.')
                left = str(min(int(left), id_range[0]))
                right = str(max(int(right), id_range[1]))
                fresh_ids[i] = (int(left), int(right))
                print('New merged range:', fresh_ids[i])
                break
            i += 1
        # if we couldnt merge it in, add it to its own range
        if i == len(fresh_ids):
            print('No overlap found, adding new range.')
            fresh_ids.append((int(left), int(right)))
        print('Now have ranges:', fresh_ids)
        print('Checking for overlapping ranges...')
        j = 0
        while j < len(fresh_ids) - 1:
            k = j + 1
            while k < len(fresh_ids):
                range_j = fresh_ids[j]
                range_k = fresh_ids[k]
                if not (range_j[1] < range_k[0] or range_j[0] > range_k[1]):
                    # overlap found so merge
                    new_left = min(range_j[0], range_k[0])
                    new_right = max(range_j[1], range_k[1])
                    fresh_ids[j] = (new_left, new_right)
                    del fresh_ids[k]
                else:
                    k += 1
            j += 1
    print('Finished defining unique fresh ids.')

    total_fresh_ids = 0
    for r in fresh_ids:
        total_fresh_ids += r[1] - r[0] + 1

    return total_fresh_ids


if __name__ == "__main__":
    print(run())
