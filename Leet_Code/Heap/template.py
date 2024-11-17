import heapq
from Leet_Code.Tree import list_to_tree_node, print_tree

# 创建一个列表
nums = [5, 7, 9, 1, 3]

print_tree(list_to_tree_node(nums))

# 将列表转换为最小堆
heapq.heapify(nums)

print_tree(list_to_tree_node(nums))

print("最小堆:", nums)  # 输出: 最小堆: [1, 3, 9, 7, 5]

# 插入一个新元素
heapq.heappush(nums, 2)
print("插入 2 后的堆:", nums)  # 输出: 插入 2 后的堆: [1, 2, 9, 7, 5, 3]
print_tree(list_to_tree_node(nums))

# 弹出最小元素
min_element = heapq.heappop(nums)
print("弹出的最小元素:", min_element)  # 输出: 弹出的最小元素: 1
print("弹出后的堆:", nums)  # 输出: 弹出后的堆: [2, 3, 9, 7, 5]
