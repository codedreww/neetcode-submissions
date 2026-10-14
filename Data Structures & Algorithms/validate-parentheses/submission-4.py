class Solution:
    def isValid(self, s: str) -> bool:
        matching = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack or stack.pop() != matching[i]:
                    return False
        if not stack:
            return True
        else:
            return False