from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        temp = 1
        l, r = 0, len(nums) - 1

        ans = [1] * len(nums)

        for i in range(len(nums)):
            ans[i] *= temp
            temp *= nums[i]

        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= temp
            temp *= nums[i]

        return ans


Solution().productExceptSelf([1, 2, 3, 4, 5])

#  1 th =       *   2*3*4*5
#  2 th = 1     *   3*4*5
#  3 th = 1*2   *   4*5
#  4 th = 1*2*3 *   5
#  5 th = 1*2*3*4


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         ans = []
#         for i in range(len(nums)):

#             ans.append( nums[:i] * nums(i:)   )



class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        # [6,5,3,1,0]
        n = len(citations)
        h = 0
        for i, v in enumerate(citations):
            if v >= n-i:
                h+=1
            else:
                break
        return h
    
Solution().hIndex([6,5,3,1,0])