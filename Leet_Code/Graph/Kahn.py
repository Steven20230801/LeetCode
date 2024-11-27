from collections import deque, defaultdict


def kahn_topological_sort(vertices, edges):
    in_degree = {i: 0 for i in range(vertices)}
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque([v for v in in_degree if in_degree[v] == 0])
    topological_order = []

    while queue:
        vertex = queue.popleft()
        topological_order.append(vertex)

        for neighbor in graph[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topological_order) == vertices:
        return topological_order
    else:
        return []  # Graph has a cycle


# def kahn_topological_sort(vertices, edges):
#     """
#     使用 Kahn 算法對有向無環圖（DAG）進行拓撲排序。

#     參數：
#     - vertices: 節點數量（整數），節點編號為 0 到 vertices - 1
#     - edges: 邊的列表，每條邊表示為 (u, v)，表示從節點 u 指向節點 v

#     返回值：
#     - 拓撲排序結果的列表；如果圖中有環，則返回空列表
#     """

#     # 初始化每個節點的入度為 0
#     in_degree = {i: 0 for i in range(vertices)}
#     # 建立圖的鄰接表表示
#     graph = defaultdict(list)

#     # 構建圖並計算每個節點的入度
#     for u, v in edges:
#         graph[u].append(v)  # 在鄰接表中添加邊
#         in_degree[v] += 1  # 目標節點的入度加 1

#     # 將所有入度為 0 的節點加入隊列
#     queue = deque([i for i in range(vertices) if in_degree[i] == 0])
#     # 用於存放拓撲排序結果的列表
#     topological_order = []

#     # 進行迭代，直到隊列為空
#     while queue:
#         # 從隊列中取出一個入度為 0 的節點
#         vertex = queue.popleft()
#         topological_order.append(vertex)  # 將該節點加入結果列表

#         # 遍歷該節點的所有相鄰節點
#         for neighbor in graph[vertex]:
#             in_degree[neighbor] -= 1  # 相鄰節點的入度減 1
#             if in_degree[neighbor] == 0:  # 如果入度為 0，加入隊列
#                 queue.append(neighbor)

#     # 如果結果列表包含了所有的節點，則拓撲排序成功
#     if len(topological_order) == vertices:
#         return topological_order
#     else:
#         return []  # 圖中存在環，無法進行拓撲排序


# Example usage:
vertices = 6
edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
print(kahn_topological_sort(vertices, edges))


print(kahn_topological_sort(vertices=4, edges=[[1, 0], [2, 0], [3, 1], [3, 2]]))
