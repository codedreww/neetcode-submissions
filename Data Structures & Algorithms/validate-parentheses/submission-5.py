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
        return not stack