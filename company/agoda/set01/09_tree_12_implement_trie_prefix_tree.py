"""Implement Trie (Prefix Tree) problem implementation."""


class TrieNode:
    """Trie node with children map and end-of-word flag."""

    def __init__(self) -> None:
        self.children: dict[str, "TrieNode"] = {}
        self.is_end = False


class Trie:
    """Trie data structure with insert, search, and startsWith operations."""

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.starts_with("app") is True
