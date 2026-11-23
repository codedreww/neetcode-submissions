from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1

        s1_dict = defaultdict(int)
        s2_dict = defaultdict(int)
        for i in s1:
            s1_dict[i] += 1
        
        for j in range (len(s1)):
            if j < len(s2):
                s2_dict[s2[j]] += 1

        while r < len(s2):
            if s1_dict == s2_dict:
                return True
            else:
                s2_dict[s2[l]] -= 1
                if s2_dict[s2[l]] == 0:
                    s2_dict.pop(s2[l])
                l += 1
                r += 1
                if r < len(s2):
                    s2_dict[s2[r]] += 1

        return False