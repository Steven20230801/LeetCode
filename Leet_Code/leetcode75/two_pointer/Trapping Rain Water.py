from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        prefix = []
        temp = 0
        for i in height:
            temp = max(i, temp)
            prefix.append(temp)

        postfix = []
        temp = 0
        for i in range(len(height) - 1, -1, -1):
            temp = max(height[i], temp)
            postfix.append(temp)
        postfix = postfix[::-1]

        # print(prefix)
        # print(postfix)
        res = 0
        for i in range(len(height)):

            res += min(prefix[i], postfix[i]) - height[i]

        return res


Solution().trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
