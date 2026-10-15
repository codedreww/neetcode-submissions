class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+', '-', '*', '/'}
        tmp1 = 0
        tmp2 = 0
        for i in tokens:
            stack.append(i)
            if i in operations:
                op = stack.pop()
                tmp1 = int(stack.pop())
                tmp2 = int(stack.pop())
                if op == "*":
                    stack.append(tmp2 * tmp1)
                elif op == "+":
                    stack.append(tmp2 + tmp1)
                elif op == "-":
                    stack.append(tmp2 - tmp1)
                elif op == "/":
                    stack.append(int(tmp2 / tmp1))
        return int(stack.pop())
            
