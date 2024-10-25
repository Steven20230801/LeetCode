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


Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
