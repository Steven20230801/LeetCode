import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [2, 7, 4, 1, 8, 1]
        res = []
        for s in stones:
            heapq.heappush(res, -s)

        while len(res) > 1:
            x = -heapq.heappop(res)
            y = -heapq.heappop(res)

            if x != y:
                heapq.heappush(res, -(x - y))

        if len(res) == 0:
            return 0
        else:
            return -res[0]
