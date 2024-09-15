from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        st = []
        for i, v in enumerate(nums2):

            while st and nums2[st[-1]] < v:
                x = st.pop()
                res[nums2[x]] = v

            st.append(i)

        return [res.get(x, -1) for x in nums1]


Solution().nextGreaterElement([1, 3, 5, 2, 4], [5, 4, 3, 2, 1])
