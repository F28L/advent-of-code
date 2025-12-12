import sys
from collections import defaultdict, deque
from dataclasses import dataclass


@dataclass(frozen=True)
class VisitState:
    visited_dac: bool
    visited_fft: bool

    def updated(self, node_name: str) -> "VisitState":
        return VisitState(
            visited_dac=self.visited_dac or node_name == "dac",
            visited_fft=self.visited_fft or node_name == "fft"
        )


class Node:
    def __init__(self, name: str):
        self.name = name
        self.neighbors: list[Node] = []

    def add_neighbor(self, neighbor: "Node"):
        self.neighbors.append(neighbor)

    def __repr__(self):
        return f"Node({self.name})"


def count_paths_dag(start: Node, end: Node, nodes: list[Node]) -> int:
    """Counts number of distinct DAG paths from start → end that visit dac & fft."""
    # build indegree to use for topology
    indegree = {n: 0 for n in nodes}
    for n in nodes:
        for neigh in n.neighbors:
            indegree[neigh] += 1

    # sort by topology so we can processed based on radius from root instead of a bfs algo
    q = deque([n for n in nodes if indegree[n] == 0])
    topo = []

    while q:
        u = q.popleft()
        topo.append(u)
        for v in u.neighbors:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    # DP: dp[node][VisitState] = count
    dp = {n: defaultdict(int) for n in nodes}
    dp[start][VisitState(False, False)] = 1

    for u in topo:
        for state, ways in dp[u].items():
            for v in u.neighbors:
                new_state = state.updated(v.name)
                dp[v][new_state] += ways

    return dp[end][VisitState(True, True)]


def run():
    raw_edges = []
    node_names = set()

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        name, neighbors_str = line.split(":", 1)
        name = name.strip()
        node_names.add(name)

        neighs = [n.strip() for n in neighbors_str.split() if n.strip()]
        for neigh in neighs:
            raw_edges.append((name, neigh))
            node_names.add(neigh)

    node_names.add("out")

    nodes_map = {name: Node(name) for name in node_names}

    for u, v in raw_edges:
        nodes_map[u].add_neighbor(nodes_map[v])

    result = count_paths_dag(nodes_map["svr"], nodes_map["out"], list(nodes_map.values()))

    return result


if __name__ == "__main__":
    print(run())