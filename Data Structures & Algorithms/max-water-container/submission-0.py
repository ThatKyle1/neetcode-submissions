class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        mostWater = 0
        
        l, r = 0, len(heights) - 1

        while l < r:
            mostWater = max((r - l) * min(heights[l],heights[r]), mostWater)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return mostWater