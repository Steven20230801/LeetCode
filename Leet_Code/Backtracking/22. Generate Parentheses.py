from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []  # 用於存儲所有有效的括號組合

        def dfs(open_count, close_count, current):
            """
            使用深度優先搜索（DFS）來生成所有有效的括號組合。

            :param open_count: 已經放置的左括號數量
            :param close_count: 已經放置的右括號數量
            :param current: 當前的括號序列
            """
            # 當所有括號都已放置且左右括號數量相等時，將當前組合加入結果中
            if open_count == close_count == n:
                res.append(current)
                return

            # 如果還可以放置左括號，則嘗試放置左括號並進行遞迴
            if open_count < n:
                dfs(open_count + 1, close_count, current + "(")

            # 如果已放置的左括號多於右括號，可以放置右括號
            if open_count > close_count:
                dfs(open_count, close_count + 1, current + ")")

        # 開始DFS，初始時左右括號數均為0，當前序列為空
        dfs(0, 0, "")
        return res
