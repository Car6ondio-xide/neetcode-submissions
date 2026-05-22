class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f = 0 
        b = len(numbers) - 1
        while f < b and numbers[f] + numbers[b] != target:
            if numbers[f] + numbers[b] > target:
                b -= 1
                continue
            if numbers[f] + numbers[b] < target:
                f += 1
                continue

        return [f+1, b+1]
