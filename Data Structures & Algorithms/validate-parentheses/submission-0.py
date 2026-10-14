class Solution:
    def isValid(self, s: str) -> bool:
        valid_char = ["(", ")", "{", "}", "[", "]"]
        open_char = ["(", "{", "[" ]
        stack = []
        for i in range (0, len(s)):
            if s[i] not in valid_char:
                return False
            stack.append(s[i])
            if s[i] not in open_char:
                stack.pop()
                if not stack:
                    return False
                if s[i] == "}" and stack[-1] == "{":
                    stack.pop()
                elif s[i] == ")" and stack[-1] == "(":
                    stack.pop()
                elif s[i] == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        else: 
            return False

