class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost[0], cost[1])
        B = [101] * len(cost)
        B[0] = cost[0]
        B[1] = cost[1]
        for k in range (2, len(cost)):
            B[k] = min(B[k - 1] + cost[k], B[k - 2] + cost[k])

        return min(B[len(cost) - 1], B[len(cost) - 2])



