"""LeetCode 205. Isomorphic Strings."""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:  # noqa: N802
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}
        for a, b in zip(s, t):
            if s_to_t.get(a, b) != b or t_to_s.get(b, a) != a:
                return False
            s_to_t[a] = b
            t_to_s[b] = a
        return True
