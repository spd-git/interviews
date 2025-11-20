from __future__ import annotations

from typing import List
from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        genes = ["A", "C", "G", "T"]
        queue = deque([(startGene, 0)])
        visited = {startGene}

        while queue:
            gene, steps = queue.popleft()
            if gene == endGene:
                return steps
            gene_list = list(gene)
            for i, original in enumerate(gene_list):
                for g in genes:
                    if g == original:
                        continue
                    gene_list[i] = g
                    new_gene = "".join(gene_list)
                    if new_gene in bank_set and new_gene not in visited:
                        visited.add(new_gene)
                        queue.append((new_gene, steps + 1))
                gene_list[i] = original
        return -1
