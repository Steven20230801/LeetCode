from typing import Counter, List


matrix = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]

transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed_matrix)


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cnt = Counter(tuple(row) for row in grid)
        return sum(cnt[col] for col in zip(*grid))


Solution().equalPairs(matrix)
