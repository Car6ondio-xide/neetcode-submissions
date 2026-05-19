class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        before = len(nums)
        after = len(set(nums))
        if before != after:
            return True
        else:
            return False
