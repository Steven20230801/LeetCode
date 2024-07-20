from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        

    def add(self, val: int) -> int: