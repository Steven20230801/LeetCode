from typing import List
from math import floor


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if len(tokens) == 1:
            return tokens[0]

        opertors = "+-*/"
        st = []

        for n in tokens:

            if n in opertors:  # 代表是加減乘除
                x = st.pop()
                y = st.pop()

                if n == "/":
                    z = int(int(y) / int(x))
                else:
                    z = eval(str(y) + n + str(x))
                st.append(z)
            else:
                st.append(n)

        return int(z)


Solution().evalRPN(["2", "1", "+", "3", "*"])
Solution().evalRPN(["4", "13", "5", "/", "+"])
Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
