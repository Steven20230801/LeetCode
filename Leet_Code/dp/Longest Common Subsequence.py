from functools import cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n = len(text1)
        m = len(text2)
        memo = {}

        def dfs(i1, i2):

            #
            if i1 == n or i2 == m:
                return 0

            if (i1, i2) in memo:
                return memo[(i1, i2)]

            if text1[i1] == text2[i2]:
                memo[(i1, i2)] = 1 + dfs(i1 + 1, i2 + 1)
            else:
                memo[(i1, i2)] = max(dfs(i1 + 1, i2), dfs(i1, i2 + 1))

            return memo[(i1, i2)]

        return dfs(0, 0)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n = len(text1)
        m = len(text2)

        @cache
        def dfs(i1, i2):

            #
            if i1 == n or i2 == m:
                return 0

            if text1[i1] == text2[i2]:
                return 1 + dfs(i1 + 1, i2 + 1)
            else:
                return max(dfs(i1 + 1, i2), dfs(i1, i2 + 1))

        return dfs(0, 0)


Solution().longestCommonSubsequence(text1="abcde", text2="ace")
