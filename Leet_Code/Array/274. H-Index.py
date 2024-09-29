from collections import Counter
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)

        # 0, 1,  3, 5, 6
        h = 0
        for i in range(n - 1, -1, -1):
            if citations[i] < n - i:  # n -i = freq
                return h
            else:
                h += 1
        return h
        # [3, 0, 1, 6, 5]
        # {0:1, 2:2, 3:3} {citation: freq}
        # postsum
        # {0:5, 2:5, 3:3} -> 3
        # 0, 1,  3, 5, 6
        # 6, 5,  3, 2, 1

    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        # 0, 1,  3, 5, 6
        l = 0
        r = n - 1
        h = 0

        while l <= r:
            m = (l + r) // 2
            num = citations[m]
            cumsum = n - m
            if num >= cumsum:
                r = m - 1
            else:
                l = m + 1

        return r  # (r+1)  = num >= cumsum


Solution().hIndex([3, 0, 1, 6, 5])
Solution().hIndex([3, 1, 1])
Solution().hIndex([100])
Solution().hIndex([0, 0, 0])
Solution().hIndex([11, 15])
Solution().hIndex([0, 0, 4, 4])

# binary search


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        # 0, 1,  3, 5, 6
        l = 0
        r = n - 1
        h = 0

        while l <= r:
            m = (l + r) // 2
            num = citations[m]
            cumsum = n - m
            if num >= cumsum:
                r = m - 1
            else:
                l = m + 1

        return n - l


Solution().hIndex([0, 1, 3, 5, 6])
