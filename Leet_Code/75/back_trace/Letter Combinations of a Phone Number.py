from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        h = {"2": ["a", "b", "c"], "3": ["d", "e", "f"]}

        s = []

        def dfs(digits, n):
            # 本次的動作
            for x in h[digits]:
                s.append(x)
            # 下次的動作
