class MinStack:
    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        minimum = float('-inf')
        if len(self.stack) > 0:
            minimum = self.stack[0]

        for i in range(len(self.stack)):
            if self.stack[i] <= minimum:
                minimum = self.stack[i]
        return minimum
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()