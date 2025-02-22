import heapq
from typing import List
from Leet_Code.Tree import print_tree, list_to_tree_node


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [0]
        for x in nums:
            heapq.heappush(self.heap, x)
        print_tree(list_to_tree_node(self.heap[1:]))

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        while len(self.heap) > k + 1:
            heapq.heappop(self.heap)
        # print_tree(list_to_tree_node(self.heap[1:]))

        return self.heap[-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
obj = KthLargest(3, [4, 5, 8, 2])
param_1 = obj.add(4)
param_1 = obj.add(4)
