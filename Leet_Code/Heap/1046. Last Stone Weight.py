import heapq
from typing import List
from Leet_Code.Tree import TreeNode, root, print_tree, list_to_tree_node


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stones = [2, 7, 4, 1, 8, 1]
        res = []
        for s in stones:
            heapq.heappush(res, -s)
        print(res)
        print_tree(list_to_tree_node(res))

        # pop 2 and destroy
        while len(res) > 1:
            x = -heapq.heappop(res)  # max     8
            y = -heapq.heappop(res)  # max 2   7
            remain = x - y  # = 1
            if remain:
                heapq.heappush(res, -remain)

        if not res:
            return 0
        else:
            return -res[-1]
