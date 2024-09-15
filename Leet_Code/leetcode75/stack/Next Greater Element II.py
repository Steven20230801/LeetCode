from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        st = []
        for i, v in enumerate(nums * 2):

            while st and nums[st[-1] % len(nums)] < v:
                x = st.pop()
                res[x % len(nums)] = v

            st.append(i)

        return res


Solution().nextGreaterElements([1, 2, 1])
Solution().nextGreaterElements([1, 2, 3, 4, 3])
Solution().nextGreaterElements([5, 4, 3, 2, 1])
