from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pright = len(s1) - 1

        let = defaultdict(int)
        let2 = defaultdict(int)

        for letter in s1:
            let[letter] += 1
    
        for i in range (len(s2) - pright):
            let2 = let.copy()
            right = pright + i
            left = i

            substr = s2[left:(right + 1)]
            for j in substr:
                if j in let2:
                    let2[j] -= 1
            if all(v == 0 for v in let2.values()):
                return True
            
        return False
                    