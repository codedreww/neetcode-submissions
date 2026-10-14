class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Normalize the string
        s = s.replace(" ", "").lower()
        
        # Filter out non-alphanumeric characters (optional, depending on your needs)
        s = ''.join(char for char in s if char.isalnum())

        # Reverse the string manually
        arr = []
        for i in range(len(s) - 1, -1, -1):  # FIX: range must go to -1 to include 0
            arr.append(s[i])
        
        new_s = ''.join(arr)
        print(f"Original: {s}")
        print(f"Reversed: {new_s}")
        return new_s == s