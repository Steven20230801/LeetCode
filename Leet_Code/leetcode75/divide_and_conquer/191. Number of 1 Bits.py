class Solution:
    def hammingWeight(self, n: int) -> int:

        def dfs(n, res):

            x, y = divmod(n, 2)

            # base case, x == 0 回傳
            if x == 0:
                return res + y

            return dfs(x, res + y)

        return dfs(n, 0)


class Solution:
    def hammingWeight(self, n):
        ans = 0
        while n:
            n &= n - 1
            ans += 1
        return ans


Solution().hammingWeight(8)
Solution().hammingWeight(11)
Solution().hammingWeight(128)
Solution().hammingWeight(11)
