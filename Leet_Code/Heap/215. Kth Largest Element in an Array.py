from heapq import heappop, heappush
from typing import List
from Leet_Code.Tree import list_to_tree_node, print_tree


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        for num in nums:
            heappush(res, -num)

        print_tree(list_to_tree_node(res))

        while len(res) > k:
            heappop(res)

        return -res[0]


Solution().findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2)
