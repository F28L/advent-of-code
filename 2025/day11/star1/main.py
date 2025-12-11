import sys
from collections import deque


class Node:
    name: str
    neighbors: list['Node']

    def __init__(self, name: str, neighbors: list['Node']=None):
        self.name = name
        self.neighbors = neighbors

    def add_neighbor(self, neighbor: 'Node'):
        if self.neighbors is None:
            self.neighbors = []
        self.neighbors.append(neighbor)

    def __repr__(self):
        return f"Node({self.name})"

    def __str__(self):
        neighbor_names = ', '.join(n.name for n in self.neighbors) if self.neighbors else 'None'
        return f"{self.name}: [{neighbor_names}]"


def run():
    nodes: dict[str, Node] = dict()
    neighbors = []
    for line in sys.stdin:
        name, neighbors_str = line.strip().split(':')
        neigh = [n for n in neighbors_str.strip().split(' ')] if neighbors_str else []
        print(name, neigh)
        nodes[name] = Node(name)
        neighbors.append(neigh)

    nodes['out'] = Node('out')

    for i, name in enumerate(list(nodes.keys())[:-1]):
        neigh_names = neighbors[i]
        for neigh_name in neigh_names:
            nodes[name].add_neighbor(nodes[neigh_name])

    # Do shortest path algo to find all possible routes from 'you' to 'out'
    q = deque()
    q.append((nodes['you'], 0))
    routes = 0
    while q:
        node = q.popleft()
        if node[0].name == 'out':
            print(f"Found path to out with length {node[1]}")
            routes += 1
            continue
        for neighbor in node[0].neighbors:
            q.append((neighbor, node[1] + 1))
    print(f"Total routes from 'you' to 'out': {routes}")
    return routes


if __name__ == "__main__":
    result = run()