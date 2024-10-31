from collections import deque
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        res = 0
        visited = [False] * len(isConnected)

        def dfs(i):

            if visited[i]:
                return
            else:
                visited[i] = True

            for j in range(len(isConnected[i])):
                if isConnected[i][j]:
                    dfs(j)

        for x in range(len(visited)):
            # print(visited)
            if not visited[x]:
                res += 1
                dfs(x)
        return res


from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # 初始化訪問標記列表，所有節點初始為未訪問
        visited = [False] * len(isConnected)
        res = 0  # 用於計數省份數量

        def dfs(i):
            # 如果當前節點已被訪問，返回
            if visited[i]:
                return

            # 標記當前節點為已訪問
            visited[i] = True

            # 遍歷與當前節點直接相連的所有節點
            for j in range(len(isConnected[i])):
                if isConnected[i][j]:
                    dfs(j)  # 對連接的節點進行深度優先搜索

        # 遍歷所有節點
        for x in range(len(visited)):
            # 如果節點 x 未被訪問，表示發現一個新的連通分量
            if not visited[x]:
                res += 1  # 增加省份計數
                dfs(x)  # 從節點 x 開始進行深度優先搜索

        return res  # 返回總的省份數量


# BFS
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        res = 0
        # 遍歷所有節點
        for x in range(len(isConnected)):
            if x not in visited:
                res += 1
                visited.add(x)
                queue = deque()
                queue.append(x)
                # x = [1, 1, 0]
                while queue:
                    xx = queue.popleft()
                    # xx = [1, 1, 0]
                    xx_connection = isConnected[xx]
                    for j in range(len(xx_connection)):
                        if j not in visited and xx_connection[j]:
                            visited.add(j)
                            queue.append(j)

        return res


# BFS GPT + 註解
from typing import List
from collections import deque


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()  # 用於記錄已訪問的城市
        res = 0  # 省份計數器

        # 遍歷所有城市
        for x in range(len(isConnected)):
            if x not in visited:
                res += 1  # 發現一個新的省份
                visited.add(x)  # 標記城市 x 為已訪問
                queue = deque()
                queue.append(x)  # 將城市 x 加入隊列進行 BFS

                # 開始 BFS 遍歷與城市 x 連通的所有城市
                while queue:
                    xx = queue.popleft()  # 取出隊列中的一個城市
                    xx_connection = isConnected[xx]  # 獲取城市 xx 的連接情況

                    # 遍歷所有與城市 xx 可能連通的城市
                    for j in range(len(xx_connection)):
                        if j not in visited and xx_connection[j]:
                            visited.add(j)  # 標記城市 j 為已訪問
                            queue.append(j)  # 將城市 j 加入隊列繼續 BFS

        return res  # 返回總的省份數量


Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
