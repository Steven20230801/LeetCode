from typing import List

from functools import cmp_to_key


# 定义一个比较函数 cmp，返回负数表示 x < y，0 表示相等，正数表示 x > y
def compare_age(person1, person2):
    return person1["age"] - person2["age"]


# 定义一个包含若干人的列表
people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}]

# 使用 cmp_to_key 将比较函数转换为 key 函数
sorted_people = sorted(people, key=cmp_to_key(compare_age))

print(sorted_people)

from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums = [str(num) for num in nums]

        def compare_str(s1, s2):
            # "990" > "909" -> 9 > 90
            #  "3 34" < "34 3"
            if s1 + s2 > s2 + s1:
                return 1
            else:
                return -1

        nums = sorted(nums, key=cmp_to_key(compare_str), reverse=True)
        res = "".join(nums)
        if int(res) != 0:
            return res
        else:
            return "0"
        # [9, 90, 99, 93] -> "9999390"


Solution().largestNumber([9, 90])
Solution().largestNumber([0, 0])
