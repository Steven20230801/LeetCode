from functools import cache


def knapsack(capacity, weights, values) -> int:
    n = len(weights)

    @cache
    def dfs(i, c):

        if i < 0:
            return 0
        # 超出容量
        if weights[i] > c:
            return dfs(i - 1, c)

        res = max(dfs(i - 1, c), dfs(i - 1, c - weights[i]) + values[i])
        return res

    return dfs(n - 1, capacity)


def knapsack(capacity, weights, values) -> int:
    n = len(weights)

    memo = {}

    def dfs(i, c):

        if (i, c) in memo:
            return memo[(i, c)]

        if i < 0:
            return 0
        # 超出容量
        if weights[i] > c:
            memo[(i, c)] = dfs(i - 1, c)
        else:
            memo[(i, c)] = max(dfs(i - 1, c), dfs(i - 1, c - weights[i]) + values[i])
        return memo[(i, c)]

    return dfs(n - 1, capacity)


# 動態規劃解法
# 時間複雜度: O(n * m)，空間複雜度: O(n * m)
# 其中 n 是物品的數量，m 是容量。
def dp(profit, weight, capacity):
    N, M = len(profit), capacity
    dp = [[0] * (M + 1) for _ in range(N)]

    # 填充第一列和第一行以減少邊界情況
    for i in range(N):
        dp[i][0] = 0
    for c in range(M + 1):
        if weight[0] <= c:
            dp[0][c] = profit[0]

    for i in range(1, N):
        for c in range(1, M + 1):
            skip = dp[i - 1][c]
            include = 0
            if c - weight[i] >= 0:
                include = profit[i] + dp[i - 1][c - weight[i]]
            dp[i][c] = max(include, skip)
    return dp[N - 1][M]


def knapsack(capacity, weights, values) -> int:
    n, m = len(values), capacity  # n 是物品的數量，m 是容量。
    # 設 dp[i][c] 表示考慮前 i 個物品，且背包剩餘容量為 c 時能夠獲得的最大總利潤。
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    # dp[0][c] = 0 當沒有物品可選擇時（即 i = 0）：
    # dp[i][0] = 0 當背包容量為 0 時

    # 填充 DP 表格
    for i in range(1, n + 1):
        for c in range(1, capacity + 1):
            if weights[i - 1] <= c:
                # 選擇不選或選擇物品 i-1，取較大者
                dp[i][c] = max(dp[i - 1][c], values[i - 1] + dp[i - 1][c - weights[i - 1]])
            else:
                # 無法選擇物品 i-1，只能不選
                dp[i][c] = dp[i - 1][c]

    # 最終，我們需要的最大總利潤為 dp[n][C]，其中 n 是物品的總數，C 是背包的最大容量。
    return dp[n][m]


knapsack(capacity=8, weights=[2, 3, 4, 5], values=[3, 4, 5, 6])
knapsack(capacity=10, weights=[2, 3, 5, 7], values=[1, 4, 5, 7])
