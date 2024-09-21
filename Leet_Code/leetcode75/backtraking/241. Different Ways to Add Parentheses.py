from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        # 如果只有数字，直接返回
        if input.isdigit():
            return [int(input)]

        res = []
        for i, char in enumerate(input):
            if char in ['+', '-', '*']:
                # 1.分解：遇到运算符，计算左右两侧的结果集
                # 2.解决：diffWaysToCompute 递归函数求出子问题的解
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                # 3.合并：根据运算符合并子问题的解
                for l in left:
                    for r in right:
                        if char == '+':
                            res.append(l + r)
                        elif char == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)

        return res


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
                    right = dfs(expr[i+1:])
                    
                    # 根据运算符，将左右部分的结果组合
                    for l in left:
                        for r in right:
                            if expr[i] == '+':
                                res.append(l + r)
                            elif expr[i] == '-':
                                res.append(l - r)
                            elif expr[i] == '*':
                                res.append(l * r)
            # 如果 res 为空，说明 expr 是一个数字
            if not res:
                res.append(int(expr))
            
            # 缓存结果
            memo[expr] = res
            return res
        
        return dfs(expression)
    
Solution().diffWaysToCompute("2-1-1")