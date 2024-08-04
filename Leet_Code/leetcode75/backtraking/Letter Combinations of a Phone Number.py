from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        # letters[2] = "abc"
        n = len(digits)
        res = []

        def enter(i, x: str):
            if i >= n:
                res.append("".join(x))
                return

            for letter in letters[int(digits[i])]:
                enter(i + 1, x=x + letter)

        enter(0, x="")

        return res


Solution().letterCombinations(digits="23")
