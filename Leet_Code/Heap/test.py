import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.heap = []
        self.k = k

        for x in nums:
            heapq.heappush(self.heap, x)

        # 只保留k個
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        # 若堆中已有 k 個元素，且新元素大於堆頂（最小值）
        elif val > self.heap[0]:
            # 先推入，再移除最小值（或直接用 heapq.heappushpop）
            heapq.heappushpop(self.heap, val)
        # 返回堆頂元素，即 kth largest
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

o = KthLargest(3, [4, 5, 8, 2])
