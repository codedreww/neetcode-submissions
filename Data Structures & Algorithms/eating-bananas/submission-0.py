class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Helper function: compute hours needed if speed = k
        def hours_needed(k: int) -> int:
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k   # integer ceil(p/k)
            return hours
        
        lo, hi = 1, max(piles)
        
        while lo < hi:
            mid = (lo + hi) // 2
            if hours_needed(mid) <= h:
                hi = mid  # mid works, try smaller
            else:
                lo = mid + 1  # mid too slow, increase
        return lo