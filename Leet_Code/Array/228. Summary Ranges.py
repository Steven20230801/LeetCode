from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        n = len(nums)
        i = 0
        while i <= n-1:

            st = nums[i]
            while i < n-1 and nums[i] + 1 == nums[i+1]:
                i += 1
            else:
                ed = nums[i]

                if st == ed:
                    path = str(st)
                else:
                    path = "->".join([str(st), str(ed)])
                res.append(path)
                i+=1

        return res 
    
# GPT
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []  # 用於存儲結果範圍
        n = len(nums)
        i = 0  # 初始化指針

        while i < n:
            st = nums[i]  # 範圍的起始點

            # 移動指針直到不再是連續的數字
            while i < n - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1

            ed = nums[i]  # 範圍的結束點

            # 根據起始點和結束點是否相同來決定範圍的表示方式
            if st == ed:
                path = str(st)
            else:
                path = f"{st}->{ed}"
            
            res.append(path)  # 添加到結果列表
            i += 1  # 移動到下一個數字

        return res  # 返回結果

            
Solution().summaryRanges(nums = [0,1,2,4,5,7])
Solution().summaryRanges(nums = [0,2,3,4,6,8,9])
Solution().summaryRanges(nums = [])