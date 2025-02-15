from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        # {1:3, 2: 2, 3:1}
        # -> freq: 3: 1
        freq = defaultdict(list)
        for v, f in counter.items():
            freq[f].append(v)

        print(freq)
        # {3:[1], 2:[2], 1:[3]}
