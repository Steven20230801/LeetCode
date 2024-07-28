class Solution:
    def mySqrt(self, x: int) -> int:
        # 9 -> 3
        # 8 -> 2
        l, r = 1, x
        while l <= r:
            mid = (l + r) // 2

            res = mid**2

            if res <= x:
                l = mid + 1
            else:
                r = mid - 1

        # print(l-1)
        return l - 1


Solution().mySqrt(9)
