class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)

        for s in strs:
            h[tuple(sorted(s))].append(s)

        return [v for v in h.values()]
