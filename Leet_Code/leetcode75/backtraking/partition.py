from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []
        n = len(s)
        def check_palindrome(s):
            return s == s[::-1]

        def dfs(i):

            if i == n:
                ans.append(path.copy())
                return
            for j in range(i, n):
                s2 = s[i:j+1]
                if check_palindrome(s2):
                    path.append(s2)
                    dfs(j+1)
                    path.pop()
        dfs(0)
        return ans
    
Solution().partition(s = "aab")