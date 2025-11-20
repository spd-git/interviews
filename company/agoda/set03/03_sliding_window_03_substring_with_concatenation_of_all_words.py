"""LeetCode 30. Substring with Concatenation of All Words."""

from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:  # noqa: N802
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)
        target = Counter(words)
        res: List[int] = []

        for offset in range(word_len):
            left = offset
            window = Counter()
            count = 0
            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right : right + word_len]
                if word in target:
                    window[word] += 1
                    count += 1
                    while window[word] > target[word]:
                        left_word = s[left : left + word_len]
                        window[left_word] -= 1
                        left += word_len
                        count -= 1
                    if count == len(words):
                        res.append(left)
                        left_word = s[left : left + word_len]
                        window[left_word] -= 1
                        left += word_len
                        count -= 1
                else:
                    window.clear()
                    count = 0
                    left = right + word_len

        return res
