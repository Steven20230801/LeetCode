from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        n = len(digits)  # 重複執行幾次
