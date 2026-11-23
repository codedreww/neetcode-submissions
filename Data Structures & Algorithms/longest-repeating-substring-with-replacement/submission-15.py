from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = defaultdict(int)
        best = 0

        for right in range(len(s)):
            count[s[right]] += 1
            high = max(count.values())
            while ((right - left) + 1 - high) > k:
                count[s[left]] -= 1
                left += 1
            best = max(best, (right - left) + 1)

        return best