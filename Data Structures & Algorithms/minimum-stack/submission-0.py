class MinStack:

    def __init__(self):
        self.items = []
        
    def push(self, val: int) -> None:
        self.items.append(val)

    def pop(self) -> None:
        self.items.pop(-1)

    def top(self) -> int:
        x = self.items[-1]
        return x 

    def getMin(self) -> int:
        return min(self.items)
        
