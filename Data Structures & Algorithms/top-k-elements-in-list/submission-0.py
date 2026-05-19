from collections import defaultdict, Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)
        for n in nums:
            hash_map[n] += 1
        return [k for k, v in Counter(hash_map).most_common(k)]
