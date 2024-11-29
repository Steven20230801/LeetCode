from typing import List

from networkx import edges


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        edges = [[1, 2], [1, 3], [2, 3]]
        pa = [i for i in range(len(edges))]
        pa
        
        for f, t in edges:
            
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 更新x的所属节点，并返回编号为x的所属节点
        def find(x: int) -> int:
            # 如果x已经为根节点了，直接返回
            # 否则就沿着所属根节点一直往上走
            if x == self.pa[x]:
                return x
            self.pa[x] = find(self.pa[x])
            return self.pa[x]

        # 合并两个节点所属区域
        def unit(x: int, y: int):
            # 将y的所属节点作为x所属节点的所属节点
            # 相当于x所在的这个子树搭到y的所在子树的根节点上
            self.pa[find(x)] = find(y)

        self.pa = list(range(len(edges)))     # self.pa[i]表示节点i+1的所属根节点; 初始self.pa[i]=i，表示节点i以自己为根节点

        for a, b in edges:
            # 获取一条边的两个节点，self.pa中的编号 = 节点编号 - 1
            a -= 1
            b -= 1
            if find(a) != find(b):
                unit(a, b)             # 如果两个节点不在一个树上，则合并
            else:
                return [a+1, b+1]      # 如果两个节点已经在一个树上，则这条边就是那条多余的边
        return [-1, -1]