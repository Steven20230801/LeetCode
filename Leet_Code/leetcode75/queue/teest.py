class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        x = [i for i in range(1, n + 1)]
        check = set()
        del_pos = 0
        while len(check) < n:
            del_pos += k
            del_pos = del_pos % len(x)
            while x[del_pos] not in x:
                del_pos += 1
                del_pos = del_pos % n
            x.remove(x[del_pos])

        return x[0]


Solution().findTheWinner(n=5, k=2)
Solution().findTheWinner(n=6, k=5)
