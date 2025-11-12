"""Group Anagrams problem implementation."""
from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """Group strings that are anagrams of each other."""
    groups = defaultdict(list)
    for word in strs:
        signature = "".join(sorted(word))
        groups[signature].append(word)
    return list(groups.values())


if __name__ == "__main__":
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted([sorted(group) for group in result]) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
