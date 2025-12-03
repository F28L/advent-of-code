import sys


def run():
    banks = []
    for line in sys.stdin:
        banks.append(line)

    bank_maxs = [0 for _ in banks]
    for b in range(len(banks)):
        bank = banks[b]
        print(f'Processing bank {b}...')
        for i in range(len(bank)-1):
            for j in range(i+1, len(bank)):
                joltage = int(str(bank[i]) + str(bank[j]))
                if bank_maxs[b] < joltage:
                    print(f'Updating bank {b} max from {bank_maxs[b]} to {joltage}')
                    bank_maxs[b] = joltage
    total = sum(bank_maxs)
    return total


if __name__ == "__main__":
    print(run())
