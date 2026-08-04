class MinStack:

    def __init__(self):
        # put in a tuple and the second element always record min
        self.stack = []
        self.global_min = ""
        
        
        

    def push(self, val: int) -> None:
        if self.global_min == "":
            self.global_min = val
        self.global_min = min(self.global_min, val)
        self.stack.append((val, self.global_min))
        

    def pop(self) -> None:
        element = self.stack.pop()
        # the global min disappeared
        if element[1] == self.global_min:
            if len(self.stack)> 0:
                self.global_min = self.stack[-1][1]
            else:
                self.global_min = ""
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]

        
