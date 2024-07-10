# class Solution {
#     public int longestConsecutive(int[] nums) {
#         // 建立一个存储所有数的哈希表，同时起到去重功能
#         Set<Integer> set = new HashSet<>();
#         for (int num : nums) {
#             set.add(num);
#         }

#         int ans = 0;
#         // 遍历去重后的所有数字
#         for (int num : set) {
#             int cur = num;
#             // 只有当num-1不存在时，才开始向后遍历num+1，num+2，num+3......
#             if (!set.contains(cur - 1)) {
#                 while (set.contains(cur + 1)) {
#                     cur++;
#                 }
#             }
#             // [num, cur]之间是连续的，数字有cur - num + 1个
#             ans = Math.max(ans, cur - num + 1);
#         }
#         return ans;
#     }
# }


from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # 儲存所有數值的集合

        ans = 0
        for num in num_set:

            cur = num

            if (
                not num - 1 in num_set
            ):  # 檢查-1 是不是不存在, 存在的話代表不用算（因為相連有一樣起始點）
                # 若不存在開始檢查+1
                while cur + 1 in num_set:
                    cur += 1
            ans = max(ans, cur - num + 1)

        return ans


# 建立hash, 記錄每個nums達到的最右邊邊界
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # 儲存所有數值的集合

        ans = 0
        for n in num_set:  # 開始針對每個數進行查找
            # 若 n-1 不在列表裡面代表他是最左邊
            if n - 1 not in num_set:
                cur = n
                # 開始找最右邊節點
                while cur + 1 in num_set:
                    cur += 1
                ans = max(ans, cur - n + 1)
        return ans


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        uf = UnionFind()

        for num in nums:
            if num not in uf.parent:
                uf.parent[num] = num
                uf.size[num] = 1

                if num - 1 in uf.parent:
                    uf.union(num, num - 1)
                if num + 1 in uf.parent:
                    uf.union(num, num + 1)

        return max(uf.size.values())


# 測試
solution = Solution()
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))  # 輸出: 4


Solution().longestConsecutive([100, 2, 99, 3, 101, 1])
