from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        b,e = 0,0
        temp = defaultdict(int)
        ret = 0

        for e in range (len(s)):
            temp[s[e]] += 1
            high_val = max(temp.values())
            while ((e - b) + 1 - high_val) > k:
                temp[s[b]] -= 1
                b += 1
            ret = max(ret, (e-b) + 1)

        return ret