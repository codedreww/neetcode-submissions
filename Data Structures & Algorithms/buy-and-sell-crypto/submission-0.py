class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, cur, best = 0, 0, 0
        for i in range (1, len(prices)):
            cur = prices[i] - prices[l]
            while prices[l] > prices[i]:
                cur -= prices[l]
                l += 1
            best = max(best, cur)
        return best