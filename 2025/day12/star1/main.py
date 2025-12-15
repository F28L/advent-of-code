import sys

def run():
    answer = 0
    with open("input.txt") as f:
        for parts in [line.strip().split() for line in f if "x" in line]:
            size = [int(x) for x in parts[0][:-1].split("x")]
            area = size[0] * size[1]
            presents = sum([int(x) for x in parts[1:]])
            answer += 1 if area >= presents*9 else 0
    return answer

if __name__ == "__main__":
    print(run())