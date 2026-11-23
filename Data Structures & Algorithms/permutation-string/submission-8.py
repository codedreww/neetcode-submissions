from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False

        need = Counter(s1)
        window = Counter(s2[:n])

        if window == need:
            return True

        for right in range(n, len(s2)):
            # character entering the window
            window[s2[right]] += 1

            # character leaving the window
            left_char = s2[right - n]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]

            if window == need:
                return True

        return False