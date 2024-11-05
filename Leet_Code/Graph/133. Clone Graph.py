from collections import defaultdict, deque
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        # node.val = 1
        # node.neighbors = [2, 4]
        res = []
        if not node:
            return None

        queue = deque([node])

        check_list = {node: Node(node.val, [])}

        while queue:

            current = queue.popleft()

            if current.neighbors:
                for neighbor in current.neighbors:

                    if neighbor not in check_list:
                        # 將node放入
                        check_list[neighbor] = Node(val=neighbor.val, neighbors=[])
                        queue.append(neighbor)

                    check_list[current].neighbors.append(check_list[neighbor])

        return check_list[node]


# GPT

from collections import deque
from typing import List, Optional


# 定義節點類別
class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List["Node"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        # 如果輸入節點為空，返回 None
        if not node:
            return None

        # 創建一個字典來保存原始節點到克隆節點的映射
        check_list = {node: Node(node.val, [])}

        # 初始化隊列，開始 BFS 遍歷
        queue = deque([node])

        # BFS 遍歷圖
        while queue:
            # 從隊列中取出當前節點
            current = queue.popleft()

            # 遍歷當前節點的所有鄰居
            for neighbor in current.neighbors:
                if neighbor not in check_list:
                    # 如果鄰居節點尚未被克隆，則克隆並加入字典
                    check_list[neighbor] = Node(neighbor.val, [])
                    # 將未被訪問的鄰居節點加入隊列以便後續處理
                    queue.append(neighbor)

                # 將克隆後的鄰居節點添加到當前克隆節點的鄰居列表中
                check_list[current].neighbors.append(check_list[neighbor])

        # 返回克隆後的起始節點
        return check_list[node]


# 創建節點
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# 連接節點
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

solution = Solution()
cloned = solution.cloneGraph(node1)
