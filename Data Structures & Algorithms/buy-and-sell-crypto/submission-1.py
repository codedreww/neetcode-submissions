class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1 = 0
        p2 = 1
        profit = 0
        curr = 0

        while p1 <= p2 and p2 < len(prices):
            curr = prices[p2] - prices[p1]
            if curr >= profit:
                profit = curr
                p2 += 1
            elif curr >= 0:
                p2 += 1
            else: 
                p1 += 1
        
        return profit