"""Add and Search Word Data Structure Design problem implementation."""
from typing import Dict


class TrieNode:
    """Trie node supporting wildcard search."""

    def __init__(self) -> None:
        self.children: Dict[str, "TrieNode"] = {}
        self.is_end = False


class WordDictionary:
    """Data structure with addWord and search (including '.') support."""

    def __init__(self) -> None:
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, index: int) -> bool:
            if index == len(word):
                return node.is_end
            char = word[index]
            if char == ".":
                return any(dfs(child, index + 1) for child in node.children.values())
            if char not in node.children:
                return False
            return dfs(node.children[char], index + 1)

        return dfs(self.root, 0)


if __name__ == "__main__":
    dictionary = WordDictionary()
    dictionary.add_word("bad")
    dictionary.add_word("dad")
    dictionary.add_word("mad")
    assert dictionary.search(".ad") is True
