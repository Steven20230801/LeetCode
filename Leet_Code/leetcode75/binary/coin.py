class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            mid = (l + r) // 2

            res = mid**2 + mid

            if res <= 2 * n:
                l = mid + 1
            else:
                r = mid - 1

        print(l - 1)


Solution().arrangeCoins(5)
Solution().arrangeCoins(8)
Solution().arrangeCoins(1)
