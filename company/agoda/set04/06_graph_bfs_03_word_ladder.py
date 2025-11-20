from __future__ import annotations

from typing import Deque, Dict, List
from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        word_len = len(beginWord)
        pattern_map: Dict[str, List[str]] = defaultdict(list)
        for word in wordList:
            for i in range(word_len):
                pattern = word[:i] + "*" + word[i + 1 :]
                pattern_map[pattern].append(word)

        queue: Deque[tuple[str, int]] = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(word_len):
                pattern = word[:i] + "*" + word[i + 1 :]
                for neighbor in pattern_map[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, length + 1))
                pattern_map[pattern] = []  # Avoid reprocessing
        return 0
