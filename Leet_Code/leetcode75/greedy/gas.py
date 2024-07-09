"""
在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

给定两个整数数组 gas 和 cost ，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一 的。


示例 1:

输入: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
输出: 3
解释:
从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可为起始索引。
示例 2:

输入: gas = [2,3,4], cost = [3,4,3]
输出: -1
解释:
你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
因此，无论怎样，你都不可能绕环路行驶一周。
 
"""

from typing import List


# 2024.7.9(可過, 超時)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        i = 3
        cap = 0

        for i in range(len(gas)):
            cap = 0
            steps = len(gas)

            while steps > 0:  # 停止點是走了N次

                cap += gas[i]  # 這站添加的油
                cap -= cost[i]  # 到下站消耗的油

                if cap < 0:
                    break

                i += 1  # 到下一站
                steps -= 1  # 剩下要走幾次

                if i == len(gas):  # 環狀
                    i = 0
            if cap >= 0:
                return i
        return -1


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 計算每個站點的淨增加
        net = [gas[i] - cost[i] for i in range(len(gas))]

        if sum(net) < 0:  # 若淨增加是負值一定跑不完
            return -1

        # 若有的話則依序計算
        st = 0  # 起始加油站
        current_sum = 0  # 目前累加

        for i in range(len(gas)):
            current_sum += net[i]

            if current_sum < 0:  # 因為跑不過了, 換加油站
                st = i + 1
                current_sum = 0  # 重置

        return st


Solution().canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2])
Solution().canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3])
Solution().canCompleteCircuit(gas=[5, 1, 2, 3, 4], cost=[4, 4, 1, 5, 1])
