import time
from heapq import heappush, heappop


class StockPrice:

    def __init__(self):
        self.record = {}
        self.timestamp: int = 0
        self.max_heap = []  # 儲存 (-price, timestamp)
        self.min_heap = []  # 儲存 (price, timestamp)

    def update(self, timestamp: int, price: int) -> None:

        self.record[timestamp] = price
        self.timestamp = max(self.timestamp, timestamp)
        heappush(self.max_heap, (-price, timestamp))
        heappush(self.min_heap, (price, timestamp))

    def current(self) -> int:
        return self.record[self.timestamp]

    def maximum(self) -> int:
        while True:
            price, timestamp = self.max_heap[0]
            if -price == self.record[timestamp]:
                return -price
            heappop(self.max_heap)

    def minimum(self) -> int:
        while True:
            price, timestamp = self.min_heap[0]
            if price == self.record[timestamp]:
                return price
            heappop(self.min_heap)


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
