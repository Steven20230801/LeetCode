class Heap:
    def __init__(self) -> None:
        self.heap = [0]  # 位置0不放東西

    def push(self, val: int):
        self.heap.append(val)
        i = len(self.heap) - 1  # 目前val的位子
        # 一直交換直到母節點 比較小為止
        # i > 1: root 就不用換了
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            # swap
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2
