class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaned_s = re.sub(r"[^a-z0-9]", "", s)
        p1 = 0
        p2 = len(cleaned_s) - 1
        half = len(cleaned_s) // 2 - 1

        while p1 <= half and p2 >= half:
            if cleaned_s[p1] == cleaned_s[p2]:
                p1 += 1
                p2 -= 1
            else:
                return False

        return True