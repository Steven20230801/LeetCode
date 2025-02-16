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

    # We read the root element since it is the element we wish to pop.
    # Next, we take the right-most node of the last level and swap it with the root node.
    # We have now maintained the structure property, but the order property is violated.
    # To fix the order property, we have to make sure that 30 finds its place.
    # To do so, we will continously swap 30 with min(left_child, right_child) until it reaches the correct position, i.e. both of it's children are greater than or equal to 30.
    # We swap 30 with 16, then 19 with 30. The resulting tree will look like the following.


h = Heap()
h.push(5)
h.push(4)
h.push(3)
print(h.heap)
print_tree(list_to_tree_node(h.heap[1:]))
h.pop()
print_tree(list_to_tree_node(h.heap[1:]))
