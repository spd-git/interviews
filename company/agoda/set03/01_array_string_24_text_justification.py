"""LeetCode 68. Text Justification."""

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:  # noqa: N802
        res = []
        i = 0
        n = len(words)

        while i < n:
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            gaps = j - i - 1
            line_words = words[i:j]

            if j == n or gaps == 0:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                total_spaces = maxWidth - sum(len(w) for w in line_words)
                space, extra = divmod(total_spaces, gaps)
                line_parts = []
                for idx, word in enumerate(line_words[:-1]):
                    line_parts.append(word)
                    spaces = space + (1 if idx < extra else 0)
                    line_parts.append(" " * spaces)
                line_parts.append(line_words[-1])
                line = "".join(line_parts)

            res.append(line)
            i = j

        return res
