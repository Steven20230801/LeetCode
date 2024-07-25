from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        st = []  # 紀錄目前字串
        res = []  # 紀錄組合

        def backtracking(o, c):
            if o == c == n:
                res.append("".join(st))
                return
            if o < n:  # 可以增加(
                st.append("(")
                backtracking(o + 1, c)
                st.pop()
            if o > c:  # 可以增加)
                st.append(")")
                backtracking(o, c + 1)
                st.pop()

        backtracking(0, 0)

        return res


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []  # 紀錄組合

        def backtracking(o, c, x):
            if o == c == n:
                res.append(x)
                return
            if o < n:  # 可以增加(
                # x += "("
                backtracking(o + 1, c, x + "(")
                # st.pop()
            if o > c:  # 可以增加)
                # x += ")"
                backtracking(o, c + 1, x + ")")
                # st.pop()

        backtracking(0, 0, "")

        return res


Solution().generateParenthesis(3)
