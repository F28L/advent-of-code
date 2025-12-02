import sys
import re


def process_inputs():
    line = sys.stdin.readline()
    pairs = line.split(sep=',')
    ranges = [pair.split(sep='-') for pair in pairs]
    return ranges


def run(ranges):
    count = 0

    for r in ranges:
        start, end = int(r[0]), int(r[1])
        # print(f'Processing {start} to {end} interval...')
        for i in range(start, end + 1):
            # print(f'Processing {i}...')
            match = re.fullmatch(r"(.+)\1+", str(i))
            if match:
                # print(f'Adding {i} to counter')
                count += i
    return count


if __name__ == "__main__":
    inputs = process_inputs()
    print(run(inputs))
