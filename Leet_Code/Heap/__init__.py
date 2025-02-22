from heapq import heappop
from Leet_Code.Tree import print_tree, list_to_tree_node


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

    def pop(self):
        # 當 heap 中沒有元素時（只有 dummy 位置），回傳 None
        if len(self.heap) == 1:
            return None

        # 取出根節點的值（最小值）
        pop_val = self.heap[1]
        # 將最後一個元素移到根節點，然後刪除最後一個元素
        self.heap[1] = self.heap.pop()
        i = 1  # 從根節點開始調整

        # 進行下濾 (sift down) 操作，確保 min-heap 的性質
        while True:
            left = 2 * i  # 左子節點的索引
            right = 2 * i + 1  # 右子節點的索引
            smallest = i  # 假設目前節點為最小

            # 若左子節點存在且比目前節點小，更新 smallest
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left

            # 若右子節點存在且比目前節點（或左子節點）小，更新 smallest
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right

            # 如果目前節點已經比左右子節點都小，則符合 min-heap，停止調整
            if smallest == i:
                break

            # 否則，將目前節點與最小的子節點交換
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            # 更新位置到交換後的子節點，繼續往下濾
            i = smallest

        # 回傳原本的根節點值（即最小值）
        return pop_val

    def heapify(self, arr, n, i):
        smallest = i  # 目前節點
        left = 2 * i  # 左子節點
        right = 2 * i + 1  # 右子節點

        # 比較左子節點
        if left < n and arr[left] < arr[smallest]:
            smallest = left

        # 比較右子節點
        if right < n and arr[right] < arr[smallest]:
            smallest = right

        # 若最小值不是自己，則交換並遞迴調整
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.heapify(arr, n, smallest)  # 遞迴調整子樹

    def build_heap(self, arr):
        n = len(arr)
        # 從最後一個非葉節點開始 (n//2)
        for i in range(n // 2, 0, -1):
            self.heapify(arr, n, i)

    def heapify2(self, arr):
        # 0-th position is moved to the end
        arr.append(arr[0])

        self.heap = arr
        cur = (len(self.heap) - 1) // 2
        while cur > 0:
            # Percolate down
            i = cur
            while 2 * i < len(self.heap):
                if 2 * i + 1 < len(self.heap) and self.heap[2 * i + 1] < self.heap[2 * i] and self.heap[i] > self.heap[2 * i + 1]:
                    # Swap right child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = tmp
                    i = 2 * i + 1
                elif self.heap[i] > self.heap[2 * i]:
                    # Swap left child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = tmp
                    i = 2 * i
                else:
                    break
            cur -= 1


h = Heap()
h.push(5)
h.push(4)
h.push(3)
print(h.heap)
print_tree(list_to_tree_node(h.heap[1:]))
h.pop()
print_tree(list_to_tree_node(h.heap[1:]))


def heapify(arr):
    """將列表 arr 轉換為最小堆。"""
    n = len(arr)
    # 從最後一個非葉節點開始，向前進行下濾操作
    # 最後一個非葉節點的索引為 n // 2 - 1
    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, i, n)


def sift_down(arr, i, n):
    """
    對索引 i 開始的節點進行下濾操作，使該子樹滿足最小堆性質。
    n 表示堆的大小（通常為列表的長度）。
    """
    while True:
        smallest = i  # 設定目前節點為最小值
        left = 2 * i + 1  # 左子節點索引
        right = 2 * i + 2  # 右子節點索引

        # 比較左子節點
        if left < n and arr[left] < arr[smallest]:
            smallest = left

        # 比較右子節點
        if right < n and arr[right] < arr[smallest]:
            smallest = right

        # 若父節點已是最小，則停止下濾
        if smallest == i:
            break

        # 交換父節點與較小的子節點
        arr[i], arr[smallest] = arr[smallest], arr[i]
        # 將指標移動到子節點位置，繼續下濾
        i = smallest


# 測試範例
if __name__ == "__main__":
    data = [5, 7, 9, 1, 3]
    heapify(data)
    print("轉換後的堆：", data)  # 輸出可能為：[1, 3, 9, 7, 5]
    print_tree(list_to_tree_node(data))
    heappop(data)
    print_tree(list_to_tree_node(data))
    heappop(data)
    print_tree(list_to_tree_node(data))
