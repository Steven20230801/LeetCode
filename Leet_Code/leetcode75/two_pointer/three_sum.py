from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        check_x = set()
        # [-4, -1, -1, 0, 1, 2]
        for x in range(n - 2):
            # y + z = -nums[i] = -4
            if nums[x] in check_x:  # 若x一樣, y, z 的組合一定一樣 跳過檢查
                continue

            if nums[x] > 0:
                break

            check_x.add(nums[x])  #

            y = x + 1
            z = n - 1

            while y < z:  # 換成 y != z 的話會超時
                if nums[y] + nums[z] == -nums[x]:
                    ans.append([nums[x], nums[y], nums[z]])
                    y += 1
                    while nums[y] == nums[y - 1] and y < z:
                        y += 1
                elif nums[y] + nums[z] < -nums[x]:
                    y += 1
                else:
                    z -= 1

        return ans


Solution().threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4])
