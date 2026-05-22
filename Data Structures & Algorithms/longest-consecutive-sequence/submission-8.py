from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        fixed_list = sorted(set(nums))
        # print(fixed_list)

        count = 1
        max_count = []
        previous = None

        for i in fixed_list:
            if previous == None :
                previous = i
                continue
            if previous+1 == i:
                count += 1
                previous = i
                continue
            previous = i
            max_count.append(count)
            count = 1
        if len(nums) == 0:
            count = 0
        max_count.append(count)
        # print(max_count)

        return max(max_count)
