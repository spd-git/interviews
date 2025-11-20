from __future__ import annotations

from typing import Dict, List, Tuple
from collections import defaultdict, deque


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph: Dict[str, List[Tuple[str, float]]] = defaultdict(list)
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        def bfs(start: str, end: str) -> float:
            if start not in graph or end not in graph:
                return -1.0
            queue = deque([(start, 1.0)])
            visited = set([start])
            while queue:
                node, prod = queue.popleft()
                if node == end:
                    return prod
                for neighbor, weight in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, prod * weight))
            return -1.0

        return [bfs(a, b) for a, b in queries]
