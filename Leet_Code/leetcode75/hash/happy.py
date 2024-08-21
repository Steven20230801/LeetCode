class Solution:
    def isHappy(self, n: int) -> bool:
        check_list = set()

        while n not in check_list:
            check_list.add(n)

            n = self.sum_of_s2(n)
            if n == 1:
                return True

        return False

    def sum_of_s2(self, number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit**2
        return total_sum


Solution().isHappy(19)
