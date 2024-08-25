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


knapsack(8, weights=[2, 3, 4, 5], values=[3, 4, 5, 6])
knapsack(capacity=10, weights=[2, 3, 5, 7], values=[1, 4, 5, 7])
