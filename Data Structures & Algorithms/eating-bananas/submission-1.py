import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def find_hours(piles: List[int], k: int):
            ret = 0
            for i in piles:
                ret += math.ceil(i/k)
            return ret

        l_k = 1
        r_k = max(i for i in piles)
        best = r_k

        while l_k <= r_k:
            mid_k = (r_k + l_k) // 2

            if find_hours(piles, mid_k) > h:
                l_k = mid_k + 1

            else:
                best = min(best, mid_k)
                r_k = mid_k - 1
        
        return best