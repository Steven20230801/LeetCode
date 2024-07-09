from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        for r, c in enumerate(grid):
            print(r, c)
            print(c)
            print(c[r])
            print(c[-r - 1])


Solution().equalPairs(grid=[[3, 2, 1], [1, 7, 6], [2, 7, 7]])


grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]

for r, c in enumerate(grid):
    print(r, c)


gain = [-5, 1, 5, 0, -7]
[0, -5, -4, 1, 1, -6]
ans = max(0, gain[0])
for i in range(1, len(gain)):
    gain[i] += gain[i - 1]
    ans = max(ans, gain[i])


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ans_l = 0
        ans_r = 0
        l, r = 0, len(nums) - 1

        while l < r:
            if ans_l >= ans_r:
                ans_r += nums[r]
                r -= 1
            else:
                ans_l += nums[l]
                l += 1

            if ans_l == ans_r and r == l:
                return l
        return -1


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        mid = (l + r) // 2

        ans_l = sum(nums[:mid])
        ans_r = sum(nums[mid + 1 :])

        while mid > 0 and mid <= len(nums):

            if ans_l == ans_r:
                return mid

            if ans_l > ans_r:
                ans_r += nums[mid]
                ans_l -= nums[mid - 1]

                mid -= 1
            else:
                ans_l += nums[mid]
                ans_r -= nums[mid + 1]

                mid += 1

        return -1


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            if left_sum == (total_sum - left_sum - num):
                return i
            left_sum += num

        return -1


Solution().pivotIndex([-1, -1, -1, -1, -1, 0])
Solution().pivotIndex([1, 7, 3, 6, 5, 6])
Solution().pivotIndex([1, 2, 3])
Solution().pivotIndex([2, 1, -1])


class Solution:
    def tribonacci(self, n: int) -> int:

        t0 = 0
        t1 = 1
        t2 = 1
        if n == 0:
            return t0
        if n < 3:
            return t1

        past1 = t2
        past2 = t1
        past3 = t0

        for i in range(n - 2):
            now = past1 + past2 + past3
            past3 = past2
            past2 = past1
            past1 = now
        return now


Solution().tribonacci(25)


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)

        cost_list = [0] * len(cost)
        cost_list[0] = cost[0]
        cost_list[1] = cost[1]

        for i in range(2, len(cost)):
            cost_list[i] = cost[i] + min(cost_list[i - 1], cost_list[i - 2])

        return min(cost_list[-1], cost_list[-2])


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)

        cost_lag1 = cost[1]
        cost_lag2 = cost[0]

        for i in range(len(cost) - 2):
            now_cost = cost[i + 2] + min(cost_lag1, cost_lag2)
            cost_lag2 = cost_lag1
            cost_lag1 = now_cost

        return min(cost_lag1, cost_lag2)


Solution().minCostClimbingStairs([100, 1, 1])  # 1

Solution().minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
