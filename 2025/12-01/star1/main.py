import sys
import re
from enum import Enum
from dataclasses import dataclass

class Direction(Enum):
    LEFT = "L"
    RIGHT = "R"

@dataclass
class Instruction:
    direction: Direction
    steps: int
    
def run():
    instructions: list[Instruction] = []
    for line in sys.stdin:
        pattern = re.compile(r'^([LR])(\d+)$')
        match = pattern.match(line)
        if match:
            direction = Direction.LEFT if match.group(1) == 'L' else Direction.RIGHT
            steps = int(match.group(2))
        else:
            print("Invalid input")
        instructions.append(Instruction(direction, steps))
    
    ptr = 50
    count_zero = 0
    for inst in instructions:
        start = ptr
        if inst.direction == Direction.LEFT:
            ptr = (ptr - inst.steps) % 100
        else: # Direction.RIGHT
            ptr = (ptr + inst.steps) % 100
        if ptr == 0:
            count_zero +=1
        print(f'Starting from {start} moved {inst.steps} {inst.direction.name} to {ptr}.')
    
    return count_zero


if __name__ == "__main__":
    ret = run()
    print(ret)