import sys
import re
from enum import Enum
from dataclasses import dataclass
import math 

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
    count_touch_zero = 0
    for inst in instructions:
        start = ptr

        if inst.direction == Direction.RIGHT:
            if start != 0:
                first = 100 - start
                if inst.steps >= first:
                    hits = 1 + (inst.steps - first) // 100
                else:
                    hits = 0
            else:
                hits = inst.steps // 100

            count_touch_zero += hits
            ptr = (ptr + inst.steps) % 100

        else:  # Direction.LEFT
            if start != 0:
                if inst.steps >= start:
                    hits = 1 + (inst.steps - start) // 100
                else:
                    hits = 0
            else:
                hits = inst.steps // 100

            count_touch_zero += hits
            ptr = (ptr - inst.steps) % 100

        print(
            f'Starting from {start} moved {inst.steps} {inst.direction.name} '
            f'to {ptr}. Touched Zero: {count_touch_zero} total time(s).'
        )
    return count_touch_zero


if __name__ == "__main__":
    ret = run()
    print(ret)