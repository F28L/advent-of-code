import sys


def process_inputs():
    line = sys.stdin.readline()
    pairs = line.split(sep=',')
    ranges = [pair.split(sep='-') for pair in pairs]
    return ranges


def run(ranges):
    count = 0

    for r in ranges:
        start, end = int(r[0]), int(r[1])
        print(f'Processing {start} to {end} interval...')
        for i in range(start, end + 1):
            # print(f'Processing {i}...')
            i_str = str(i)
            num_digits = len(i_str)
            # looking for sequences repeated twice so first half has to equal second half
            if num_digits % 2 == 0:
                half = num_digits // 2
                left_half, right_half = i_str[0:half], i_str[half:]
                if left_half == right_half:
                    print(f'Adding {i} to counter')
                    count += i

    return count


if __name__ == "__main__":
    inputs = process_inputs()
    print(run(inputs))
