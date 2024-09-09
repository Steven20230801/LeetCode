import queue
from typing import Counter, List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)
        counter = Counter(nums)

        def dfs(i, counter):
            if i == n:
                ans.append(path.copy())
                return
            
            for x, v in counter.items():
                
                
                if counter[x] > 0:
                    path.append(x)
                    counter[x] -= 1
                    dfs(i + 1, counter)
                    counter[x] += 1
                    path.pop()

        dfs(0, counter)

        return ans


Solution().permute([1, 1, 2])
