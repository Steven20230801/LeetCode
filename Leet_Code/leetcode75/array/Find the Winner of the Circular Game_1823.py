class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        x = [i for i in range(1, n + 1)]
        n = len(x)
        check = set()
        del_pos = -1
        while len(x) > 1:
            del_pos = (del_pos + k) % n
            while del_pos in check:
                del_pos = (del_pos + 1) % n
            x.pop(del_pos)

        return x[0]


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        x = [i for i in range(1, n + 1)]  # 初始化列表 1 到 n
        del_pos = 0  # 从第一个位置开始

        while len(x) > 1:  # 当列表长度大于 1 时继续删除
            del_pos = (del_pos + k - 1) % len(x)  # 计算需要删除的索引
            x.pop(del_pos)  # 删除该索引的元素

        return x[0]  # 返回最后剩下的元素


Solution().findTheWinner(n=5, k=2)  # 3
Solution().findTheWinner(n=6, k=5)  # 1
