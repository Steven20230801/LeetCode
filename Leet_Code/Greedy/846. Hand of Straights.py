from collections import defaultdict
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        n = len(hand)
        if n % groupSize:
            return False

        h = defaultdict(int)
        for i in range(n):
            h[hand[i]] += 1

        while len(h) > 0:

            cur = min(h)

            for _ in range(groupSize):
                if h[cur] > 0:
                    h[cur] -= 1
                    if h[cur] == 0:
                        h.pop(cur)
                    cur += 1
                else:
                    return False
        return True


Solution().isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize=3)
Solution().isNStraightHand(hand=[1, 2, 3, 4, 5], groupSize=4)
