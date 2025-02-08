class StockPrice:

    def __init__(self):
        self.record = {}
        self.timestamp: int = 0
        self.max: int = 0
        self.min: int = 0

    def update(self, timestamp: int, price: int) -> None:
        self.record[timestamp] = price
        self.timestamp = timestamp
        self.max = max(self.max, price)
        self.min = min(self.min, price)

    def current(self) -> int:
        return self.record[self.timestamp]

    def maximum(self) -> int:
        return self.max

    def minimum(self) -> int:
        return self.min


st = StockPrice()
st.update(1, 10)
st.update(2, 5)
print(st.current())
print(st.maximum())
print(st.minimum())
st.update(1, 3)
print(st.current())
print(st.maximum())


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
