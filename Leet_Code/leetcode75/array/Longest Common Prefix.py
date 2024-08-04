from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for string in zip(*strs):  # 跟後續的字串比較
            if all(element == string[0] for element in string):  # 若都一樣
                res += string[0]
            else:
                return res
        return res


Solution().longestCommonPrefix(["ab", "a", ""])
Solution().longestCommonPrefix(["aaa", "aa", "aaa"])


for ss in zip(*["abc", "bd", "x"]):
    print(ss)
