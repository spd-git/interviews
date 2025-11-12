"""Clone Graph problem implementation."""
from collections import deque
from typing import Dict, Optional


class Node:
    """Graph node definition for undirected graph."""

    def __init__(self, val: int = 0, neighbors: Optional[list["Node"]] = None):
        self.val = val
        self.neighbors = neighbors or []

    def __repr__(self) -> str:  # pragma: no cover - debug helper
        return f"Node({self.val})"


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    """Breadth-first traversal to clone the entire graph."""
    if not node:
        return None

    clones: Dict[Node, Node] = {node: Node(node.val)}
    queue = deque([node])
    while queue:
        current = queue.popleft()
        for neighbor in current.neighbors:
            if neighbor not in clones:
                clones[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            clones[current].neighbors.append(clones[neighbor])
    return clones[node]
