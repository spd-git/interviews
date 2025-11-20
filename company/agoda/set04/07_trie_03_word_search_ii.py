from __future__ import annotations

from typing import Dict, List, Set


directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class TrieNode:
    def __init__(self):
        self.children: Dict[str, "TrieNode"] = {}
        self.word: str | None = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                node = node.children.setdefault(ch, TrieNode())
            node.word = word

        rows, cols = len(board), len(board[0]) if board else 0
        found: Set[str] = set()
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r: int, c: int, node: TrieNode) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c]:
                return
            ch = board[r][c]
            if ch not in node.children:
                return
            visited[r][c] = True
            next_node = node.children[ch]
            if next_node.word:
                found.add(next_node.word)
            for dr, dc in directions:
                dfs(r + dr, c + dc, next_node)
            visited[r][c] = False

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return list(found)
