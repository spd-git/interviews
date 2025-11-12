"""Word Search II problem implementation."""
from typing import Dict, List


class TrieNode:
    """Trie node storing children and word marker."""

    def __init__(self) -> None:
        self.children: Dict[str, "TrieNode"] = {}
        self.word: str | None = None


def find_words(board: List[List[str]], words: List[str]) -> List[str]:
    """Use trie and backtracking to find all words in the board."""
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.word = word

    rows, cols = len(board), len(board[0]) if board else 0
    found: List[str] = []

    def backtrack(r: int, c: int, node: TrieNode) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        char = board[r][c]
        if char == "#" or char not in node.children:
            return
        next_node = node.children[char]
        if next_node.word:
            found.append(next_node.word)
            next_node.word = None  # avoid duplicates
        board[r][c] = "#"
        backtrack(r + 1, c, next_node)
        backtrack(r - 1, c, next_node)
        backtrack(r, c + 1, next_node)
        backtrack(r, c - 1, next_node)
        board[r][c] = char

    for r in range(rows):
        for c in range(cols):
            backtrack(r, c, root)
    return found


if __name__ == "__main__":
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    assert sorted(find_words(board, ["oath", "pea", "eat", "rain"])) == ["eat", "oath"]
