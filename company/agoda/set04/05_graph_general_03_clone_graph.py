from __future__ import annotations

from typing import Dict, List, Optional


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List["Node"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None
        clones: Dict[Node, Node] = {}

        def dfs(current: Node) -> Node:
            if current in clones:
                return clones[current]
            copy = Node(current.val)
            clones[current] = copy
            for neighbor in current.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node)
