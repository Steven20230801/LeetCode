from collections import defaultdict, Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l, r = 0, len(p)
        res = []
        check_list = Counter(p)  # {c:1, b:1, a:1}
        counter = Counter(s[0:r])

        if check_list == counter:
            res.append(0)

        for r in range(r, len(s)):

            counter[s[l]] -= 1
            if not counter[s[l]]:
                counter.pop(s[l])

            l += 1
            counter[s[r]] += 1
            if counter == check_list:
                res.append(l)

        return res


Solution().findAnagrams(s="cbaebabacd", p="abc")
