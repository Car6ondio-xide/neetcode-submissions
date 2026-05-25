class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_l = 0
        max_r = 0

        water = 0

        while l < r:
            L = height[l]
            R = height[r]
            # print(f"L, R: {L, R}")
            # print(f"max_l, max_r : {max_l, max_r}")
            # print(f"l, r : {l, r}")
            # print(f"water : {water}")
            # print("=" * 10)
            if L <= R:
                if max_l > L:
                    water += max_l - L
                else:
                    max_l = L
                l += 1
            elif L > R:
                if max_r > R:
                    water += max_r - R
                else:
                    max_r = R
                r -= 1
        return water
