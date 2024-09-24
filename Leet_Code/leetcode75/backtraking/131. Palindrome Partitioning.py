from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        path = []

        def dfs(i):

            if i == n:
                ans.append(path.copy())
                return 

            for j in range(i, n+1):
                ss = s[i:j+1] 
                if ss == ss[::-1]:
                    path.append(ss)
                    dfs(j+1)
                    path.pop()
            
        dfs(0)
        return ans
    
Solution().partition("aab")
