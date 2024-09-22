from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        # 定义一个缓存字典，避免重复计算
        memo = {}

        def dfs(expr):

            if expr in memo:
                return memo[expr]

            res = []

            for i in range(len(expr)):
                if expr[i] in "+-*":
                    # 递归计算左右两部分的所有可能值
                    left = dfs(expr[:i])
                    right = dfs(expr[i + 1 :])

                    # 根据运算符，将左右部分的结果组合
                    for l in left:
                        for r in right:
                            if expr[i] == "+":
                                res.append(l + r)
                            elif expr[i] == "-":
                                res.append(l - r)
                            elif expr[i] == "*":
                                res.append(l * r)
            # 如果 res 为空，说明 expr 是一个数字
            if not res:
                res.append(int(expr))

            # 缓存结果
            memo[expr] = res
            return res

        return dfs(expression)


Solution().diffWaysToCompute(expression="2+1")
Solution().diffWaysToCompute(expression="2-1-1")
Solution().diffWaysToCompute(expression="2*3-4*5")
