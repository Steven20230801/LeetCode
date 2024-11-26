from collections import defaultdict
import heapq
from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        paths = defaultdict(list)
        for source, target in roads:
            paths[source].append(target)
            paths[target].append(source)
        # print(paths)

        maximum_heap = []
        for k, v in paths.items():
            heappush(maximum_heap, (-len(v), k))
        # print(maximum_heap)

        imp = {}
        score = n
        while maximum_heap:
            v, k = heappop(maximum_heap)
            imp[k] = score
            score -= 1
        # printscore

        res = 0
        for i in range(n):
            res += imp.get(i, 0) * len(paths[i])

        return res
