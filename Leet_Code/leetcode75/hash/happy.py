class Solution:
    def isHappy(self, n: int) -> bool:
        # 1 10 100 1000 10000
        h = {}

        def sq(n: int):
            temp = 0
            c = []
            for i in str(n):
                temp += int(i) ** 2
                c.append(i)
            return temp, tuple(c)

        ans, c = sq(n)

        if ans == 1:
            return True

        h[c] = 1

        while ans != 1:
            ans, c = sq(ans)

            if ans == 1:
                return True

            if c in h:
                return False
            else:
                h[c] = 1


Solution().isHappy(19)
