from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return [""]
        res = []
        n = len(digits)
        path = []
        letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def dfs(i):

            if i == n:
                res.append("".join(path.copy()))
                return

            for letter in letters[int(digits[i])]:
                path.append(letter)
                dfs(i + 1)
                path.pop()

        dfs(0)
        return res


Solution().letterCombinations("23")
