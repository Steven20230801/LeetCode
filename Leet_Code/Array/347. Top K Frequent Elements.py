from collections import defaultdict
from typing import Counter, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freqs = [[] for _ in range(len(nums) + 1)]
        for v, f in counter.items():
            freqs[f].append(v)

        res = []
        for i in range(len(nums), -1, -1):
            if k > 0:
                res.extend(freqs[i])
                k -= len(freqs[i])
            else:
                return res
        return res


Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)
Solution().topKFrequent([1], 1)
