from __future__ import annotations

from typing import Dict


class WordDictionary:
    def __init__(self):
        self.children: Dict[str, "WordDictionary"] = {}
        self.is_word = False

    def addWord(self, word: str) -> None:
        node = self
        for ch in word:
            node = node.children.setdefault(ch, WordDictionary())
        node.is_word = True

    def search(self, word: str) -> bool:
        return self._search_recursive(word, 0, self)

    def _search_recursive(self, word: str, index: int, node: "WordDictionary") -> bool:
        if index == len(word):
            return node.is_word
        ch = word[index]
        if ch == ".":
            return any(self._search_recursive(word, index + 1, child) for child in node.children.values())
        if ch not in node.children:
            return False
        return self._search_recursive(word, index + 1, node.children[ch])
