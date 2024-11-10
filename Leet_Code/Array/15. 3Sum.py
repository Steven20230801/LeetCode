from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums = [-1, -1, -1, -1, 0, 0, 0, 0, 0, 1, 1]
        nums.sort()
        check_x = set()
        res = []
        for x in range(len(nums)):
            if nums[x] not in check_x:
                check_x.add(nums[x])
                # two pointer of 2 sum
                y = x + 1
                z = len(nums) - 1
                print(y, z)

                while y < z:

                    sum_ = nums[y] + nums[z]

                    if sum_ == -nums[x]:
                        res.append([nums[x], nums[y], nums[z]])
                        y += 1
                        z -= 1
                        while y < z and nums[y] == nums[y - 1]:
                            y += 1
                        while z > y and nums[z] == nums[z + 1]:
                            z -= 1
                    elif sum_ < -nums[x]:
                        y += 1
                    else:
                        z -= 1

        return res


# GPT

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for x in range(n):
            # 跳過重複的第一個數
            if x > 0 and nums[x] == nums[x - 1]:
                continue

            # 如果當前數字大於0，後面不可能有三數之和為0
            if nums[x] > 0:
                break

            y, z = x + 1, n - 1  # 初始化雙指針

            while y < z:
                current_sum = nums[y] + nums[z]
                target = -nums[x]

                if current_sum == target:
                    res.append([nums[x], nums[y], nums[z]])
                    y += 1
                    z -= 1

                    # 跳過重複的左指針數字
                    while y < z and nums[y] == nums[y - 1]:
                        y += 1
                    # 跳過重複的右指針數字
                    while y < z and nums[z] == nums[z + 1]:
                        z -= 1
                elif current_sum < target:
                    y += 1  # 需要更大的數字，移動左指針
                else:
                    z -= 1  # 需要更小的數字，移動右指針

        return res


Solution().threeSum(nums=[-1, -1, -1, -1, 0, 0, 0, 0, 0, 1, 1])
