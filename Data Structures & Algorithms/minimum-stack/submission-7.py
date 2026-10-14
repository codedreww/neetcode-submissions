class MinStack:

    def __init__(self):
        self.stack = []
        self.min_var = 2**31 - 1
        self.min_index = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min_var:
            self.min_var = val
            self.min_index.append(len(self.stack) - 1)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.min_var:
            self.min_index.pop()
            if self.min_index:
                self.min_var = self.stack[self.min_index[-1]]
            else:
                self.min_var = 2**31 - 1
        return x

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.min_var
