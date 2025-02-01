from collections import Counter, defaultdict
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        counter = defaultdict(int)
        for x in hand:
            counter[x] += 1

        for x, freq in counter.items():

            # 本次循環
            while freq > 0:
                freq -= 1
                y = x
                for _ in range(groupSize - 1):

                    y += 1
                    if counter[y] == 0:
                        return False
                    else:
                        counter[y] -= 1

        return True


Solution().isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize=3)
