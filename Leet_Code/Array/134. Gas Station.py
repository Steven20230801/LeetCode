from typing import List


from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        # 遍歷每個可能的起始點
        for start in range(n):
            tank = gas[start]  # 初始化油箱為起始點的油量
            current = start  # 當前站點
            completed = True  # 標記是否能完成一圈

            # 嘗試從當前起始點走完整個迴圈
            for _ in range(n):
                cost_index = current % n  # 當前站點的成本索引
                next_station = (current + 1) % n  # 下一個站點的索引
                tank -= cost[cost_index]  # 消耗前往下一站的油量

                # 如果油量不足，無法從此起始點出發
                if tank < 0:
                    completed = False
                    break

                tank += gas[next_station]  # 加上下一站的油量
                current = next_station  # 移動到下一站

            # 如果能完成一圈，返回起始點
            if completed:
                return start

        # 如果沒有任何起始點能完成一圈，返回 -1
        return -1


# 優化思路：

# 如果從某個起始點 A 出發無法到達 B，則從 A 到 B 之間的任何點作為起始點都無法成功。這是因為累積油量在 A 到 B 之間是負的。
# 因此，我們可以跳過 A 到 B 之間的所有點，直接從 B 的下一個點作為新的起始點。

Solution().canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2])
Solution().canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3])
