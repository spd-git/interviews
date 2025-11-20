"""LeetCode 290. Word Pattern."""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:  # noqa: N802
        words = s.split()
        if len(pattern) != len(words):
            return False

        p_to_w = {}
        w_to_p = {}
        for p, w in zip(pattern, words):
            if p_to_w.get(p, w) != w or w_to_p.get(w, p) != p:
                return False
            p_to_w[p] = w
            w_to_p[w] = p
        return True
