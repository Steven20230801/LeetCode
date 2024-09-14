from collections import deque


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
        x = [i for i in range(1, n + 1)]  # 初始化 1 到 n
        del_pos = 0  # 從第一個位置開始計算

        while len(x) > 1:  # 持續做刪除, 直到只剩一個元素為止
            del_pos = (del_pos + k - 1) % len(x)  # 從刪除元素後的索引開始加, 只需要加k-1個
            x.pop(del_pos)  # 删除该索引的元素

        return x[0]


# [1,2,3,4,5]
# [2,3,4,5,1]
# [3,4,5,1]
#
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque()

        for i in range(1, n + 1):
            q.append(i)

        while len(q) > 1:

            for i in range(k - 1):

                ppl = q.popleft()
                q.append(ppl)
            q.popleft()

        return q[0]


Solution().findTheWinner(n=5, k=2)  # 3
Solution().findTheWinner(n=6, k=5)  # 1
