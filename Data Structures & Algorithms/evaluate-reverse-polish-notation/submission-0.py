class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        eval = []
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        for i in tokens:
            if i in ops:
                val2 = eval.pop()
                val1 = eval.pop()
                eval.append(ops[i](val1, val2))
                continue
            eval.append(int(i))
        return eval.pop()

                    
                        


                    
        