import sys
import heapq
from typing import Optional


class Circuit:
    def __init__(self, points):
        self.points = points

    def merge(self, other):
        self.points |= other.points


class Point:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        self.circuit: Optional[Circuit] = None

    def dist(self, other):
        return ((self.x - other.x)**2 +
                (self.y - other.y)**2 +
                (self.z - other.z)**2) ** 0.5


class Edge:
    def __init__(self, length, source, target):
        self.length = length
        self.source = source
        self.target = target

    def __lt__(self, other):
        return self.length < other.length


def run():
    coords = []
    for line in sys.stdin:
        x, y, z = map(int, line.strip().split(","))
        coords.append(Point(x, y, z))

    edges = []
    n = len(coords)

    for i in range(n):
        for j in range(i + 1, n):
            p, q = coords[i], coords[j]
            heapq.heappush(edges, Edge(p.dist(q), p, q))

    circuits = set()
    successful = 0
    print(f'Total edges to process: {len(edges)}.')
    while successful < 10 and edges:
        edge = heapq.heappop(edges)
        source, target = edge.source, edge.target
        print(f'Processing edge of length {round(edge.length, 2)} between ',
              f'({source.x},{source.y},{source.z}) and ',
              f'({target.x},{target.y},{target.z}).')
        circ_a, circ_b = source.circuit, target.circuit

        if circ_a is None and circ_b is None:
            new_circuit = Circuit({source, target})
            source.circuit = new_circuit
            target.circuit = new_circuit
            circuits.add(new_circuit)
            print(f'Created new circuit with points: ',
                  f'({source.x},{source.y},{source.z}) and ',
                  f'({target.x},{target.y},{target.z}).')
        elif circ_a is not None and circ_b is None:
            circ_a.points.add(target)
            target.circuit = circ_a
            print(f'Added point ({target.x},{target.y},{target.z}) to existing circuit.')
        elif circ_a is None and circ_b is not None:
            circ_b.points.add(source)
            source.circuit = circ_b
            print(f'Added point ({source.x},{source.y},{source.z}) to existing circuit.')
        elif circ_a != circ_b:
            circ_a.merge(circ_b)
            for p in circ_b.points:
                p.circuit = circ_a
            circuits.remove(circ_b)
            print(f'Merged two circuits.')
            print(f'New circuit size: {len(circ_a.points)} points.')
            print(f'Total number of circuits: {len(circuits)}.')

        successful += 1

    sizes = sorted((len(c.points) for c in circuits), reverse=True)

    return sizes[0] * sizes[1] * sizes[2]


if __name__ == "__main__":
    result = run()
    print(result)