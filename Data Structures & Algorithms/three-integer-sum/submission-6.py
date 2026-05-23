class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums_sorted = sorted(nums)
        for i, target in enumerate(nums_sorted):
            new_nums = nums_sorted[i+1:]
            if len(new_nums) < 2:
                break
            l = 0
            r = len(new_nums) -1
            while l < r:
                current_sum = new_nums[l] + new_nums[r]
                if current_sum < -target:
                    l += 1
                elif current_sum > -target:
                    r -= 1
                else:
                    combination = [target, new_nums[l], new_nums[r]]
                    output.append(combination)
                    l += 1
                    r -= 1
                # break


        output = [list(x) for x in list(set([tuple(x) for x in output]))]
        return output
