from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for s in strs:

            sss = list(s)
            sss.sort()

            if tuple(sss) in h:
                h[tuple(sss)].append(s)
            else:
                h[tuple(sss)] = [s]
        return [v for k, v in h.items()]


Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
