import sys


def run():
    banks = []
    for line in sys.stdin:
        banks.append(line.strip())

    bank_maxs = [0 for _ in banks]
    for b in range(len(banks)):
        bank = banks[b]
        print(f'Processing bank {b}...')
        best = []
        to_remove = len(bank) - 12
        for battery in bank:
            while len(best) > 0 and to_remove > 0 and best[-1] < battery:
                print(f'Removing {best[-1]} to add {battery}.')
                best.pop()
                to_remove -= 1
                print(f'Remaining removals: {to_remove}')
                print(best)
            best.append(battery)
            print(f'Best so far: {"".join(best)}')

        # The first 12 digits are my best possible joltage
        bank_jolt = int(''.join(best[:12]))

        print(f'Setting bank {b} max to {bank_jolt}.')
        bank_maxs[b] = bank_jolt

    total = sum(bank_maxs)
    return total


if __name__ == "__main__":
    print(run())
