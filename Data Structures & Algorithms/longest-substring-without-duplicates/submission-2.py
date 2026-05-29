class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_length = 0
        hash_map = []


        while r < len(s) and l <= r:
            while s[r] in hash_map:
                l += 1
                hash_map = s[l:r]
                # print(hash_map)
            hash_map = s[l:r+1]
            max_length = max(max_length, len(hash_map))
            r += 1

        return max_length
