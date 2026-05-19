class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for t in strs:
            key = "".join(sorted(t))
            if key in hash_map.keys():
                hash_map[key].append(t)
            else:
                hash_map[key] = [t]

        return list(hash_map.values())
