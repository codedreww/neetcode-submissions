class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxVal = 0
        right = 0
        strSet = set()

        for left in range(0, len(s)):
            while (right < len(s)) and (s[right] not in strSet):
                strSet.add(s[right])
                right += 1
            if maxVal < right - left:
                maxVal = right - left
            strSet.remove(s[left])
            left += 1

        return maxVal

