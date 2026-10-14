class MinStack:

    def __init__(self):
        self.items = []
        self.items2 = []
        
    def push(self, val: int) -> None:
        self.items.append(val)
        if not self.items2:
            self.items2.append(val)
        else:
            self.items2.append(min(val, self.items2[-1]))

    def pop(self) -> None:
        self.items.pop(-1)
        self.items2.pop(-1)

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.items2[-1]
        
