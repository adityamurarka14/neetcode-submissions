class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        # self.stack.append(val)
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            self.min = min(val, self.min)

    def pop(self) -> None:
        # self.stack.pop()
        if not self.stack:
            return
        
        pop = self.stack.pop()
        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        # return self.stack[-1]
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        # temp = []
        # mini = self.stack[-1]

        # while len(self.stack):
        #     mini = min(mini, self.stack[-1])
        #     temp.append(self.stack.pop())
        
        # while len(temp):
        #     self.stack.append(temp.pop())
        
        # return mini
        return self.min
