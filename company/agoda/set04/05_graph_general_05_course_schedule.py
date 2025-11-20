from __future__ import annotations

from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        visited = 0
        while queue:
            node = queue.popleft()
            visited += 1
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return visited == numCourses
