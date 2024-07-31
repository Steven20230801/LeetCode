from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        res = 0
        l, r = 0, 0
        f = {}
        remain = 2
        while r < len(fruits):

            if f.get(fruits[r], 0) == 0:
                remain -= 1

            f[fruits[r]] = f.get(fruits[r], 0) + 1

            while remain < 0:

                f[fruits[l]] -= 1

                if f[fruits[l]] == 0:
                    remain += 1
                    l += 1
                    break
                else:
                    l += 1

            res = max(res, r - l + 1)
            r += 1

        return res


Solution().totalFruit(fruits=[0, 1, 2, 2])
