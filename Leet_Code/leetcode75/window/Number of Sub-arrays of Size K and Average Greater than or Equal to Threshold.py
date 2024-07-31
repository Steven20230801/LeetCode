from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        l = 0
        temp = sum(arr[:k])
        res = 1 if temp >= k * threshold else 0
        for r in range(k, len(arr)):

            temp += arr[r]
            temp -= arr[l]

            if temp >= k * threshold:
                res += 1
            l += 1
        return res


Solution().numOfSubarrays(arr=[11, 13, 17, 23, 29, 31, 7, 5, 2, 3], k=3, threshold=5)

Solution().numOfSubarrays(arr=[2, 2, 2, 2, 5, 5, 5, 8], k=3, threshold=4)
