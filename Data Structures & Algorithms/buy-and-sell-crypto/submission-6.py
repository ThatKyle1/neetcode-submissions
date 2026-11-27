class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        rMaxP = 0 
        l, r = 0, 1

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                rMaxP = max(rMaxP, (prices[r] - prices[l]))
                r += 1
        return rMaxP
