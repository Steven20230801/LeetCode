from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # rooms = [[1], [2], [3], []]
        visited = [False for x in range(len(rooms))]
        print((rooms))

        def dfs(i):

            if visited[i]:
                return
            else:
                visited[i] = True

            keys = rooms[i]

            for key in keys:
                dfs(key)

        dfs(0)

        return sum(visited) == len(rooms)


# GPT
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # 初始化访问记录数组，表示每个房间是否被访问过
        visited = [False for _ in range(len(rooms))]
        # 打印输入的房间列表（可删除，用于调试）
        # print(rooms)

        # 定义深度优先搜索函数
        def dfs(i):
            if visited[i]:
                return  # 如果房间已被访问，结束递归
            else:
                visited[i] = True  # 标记当前房间为已访问

            keys = rooms[i]  # 获取当前房间的钥匙列表

            for key in keys:
                dfs(key)  # 递归访问通过钥匙能到达的房间

        dfs(0)  # 从房间 0 开始进行深度优先搜索

        return sum(visited) == len(rooms)  # 检查是否所有房间都被访问


Solution().canVisitAllRooms(rooms=[[1], [2], [3], []])
