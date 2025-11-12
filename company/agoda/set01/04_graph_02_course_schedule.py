"""Course Schedule problem implementation."""
from collections import defaultdict, deque
from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """Kahn's algorithm for topological sorting."""
    graph = defaultdict(list)
    indegree = [0] * num_courses
    for dest, src in prerequisites:
        graph[src].append(dest)
        indegree[dest] += 1

    queue = deque(i for i, deg in enumerate(indegree) if deg == 0)
    visited = 0
    while queue:
        course = queue.popleft()
        visited += 1
        for neighbor in graph[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return visited == num_courses


if __name__ == "__main__":
    assert can_finish(2, [[1, 0]]) is True
