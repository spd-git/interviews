"""Alien Dictionary problem implementation."""
from collections import defaultdict, deque
from typing import Dict, List, Set


def alien_order(words: List[str]) -> str:
    """Return a valid ordering of letters given sorted alien dictionary words."""
    graph: Dict[str, Set[str]] = defaultdict(set)
    indegree: Dict[str, int] = {char: 0 for word in words for char in word}

    for first, second in zip(words, words[1:]):
        if len(first) > len(second) and first.startswith(second):
            return ""  # invalid order
        for c1, c2 in zip(first, second):
            if c1 != c2:
                if c2 not in graph[c1]:
                    graph[c1].add(c2)
                    indegree[c2] += 1
                break

    queue = deque([char for char, deg in indegree.items() if deg == 0])
    order = []
    while queue:
        char = queue.popleft()
        order.append(char)
        for neighbor in graph[char]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != len(indegree):
        return ""
    return "".join(order)


if __name__ == "__main__":
    assert alien_order(["wrt", "wrf", "er", "ett", "rftt"]) in {"wertf"}
