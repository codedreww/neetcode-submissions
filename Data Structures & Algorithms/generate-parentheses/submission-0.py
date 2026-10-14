# 22 September 2025
# Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/description/
# Medium


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add opne paranthesis if open < n
        # only add a closing paranthesis if closed < open
        # valid IIF open == closed == n

        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res


# Holy, this is confusing, i need to learn more....
