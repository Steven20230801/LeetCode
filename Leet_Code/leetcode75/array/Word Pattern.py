class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        if len(words) != len(pattern):
            return False

        wtop = {}
        ptow = {}
        for i in range(len(pattern)):

            if pattern[i] not in ptow and words[i] not in wtop:
                wtop[words[i]] = pattern[i]
                ptow[pattern[i]] = words[i]

            else:
                if ptow.get(pattern[i]) != words[i] or wtop.get(words[i]) != pattern[i]:
                    return False

        return True


Solution().wordPattern(pattern="abba", s="dog cat cat dog")
Solution().wordPattern(pattern="abba", s="dog dog dog dog")
Solution().wordPattern(pattern="a", s=" ")
