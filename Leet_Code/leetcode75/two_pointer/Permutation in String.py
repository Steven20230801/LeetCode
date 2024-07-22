from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        temp = counter.copy()
        tempcnt = cnt = len(s1)
        L = 0
        for R in range(len(s2)):

            # 檢查是否在字典中
            if s2[R] in counter:

                if temp[s2[R]] > 0:
                    # 檢查目前的temp是否還有餘裕放下(temp[s2[R]] > 0)
                    temp[s2[R]] -= 1
                    tempcnt -= 1
                    if tempcnt == 0:
                        return True
                else:
                    while s2[L] != s2[R]:
                        temp[s2[L]] += 1
                        tempcnt += 1
                        L += 1
                    L += 1

            else:
                temp = counter.copy()
                tempcnt = cnt

        return False


Solution().checkInclusion(s1="adc", s2="dcda")
Solution().checkInclusion(s1="babcb", s2="bbbbcadf")
