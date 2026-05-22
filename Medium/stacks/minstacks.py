class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack is None:
            return
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            return None
        return min(self.stack)

# Time complexity O(1)
# Space coplexity O(n)

# Another solution
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.min_val = val
            self.stack.append(val)
        elif val < self.min_val:
            encoded_val = 2 * val - self.min_val
            self.stack.append(encoded_val)
            self.min_val = val 
        else:
            self.stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
        
        top_val = self.stack.pop()

        if top_val < self.min_val:
            self.min_val = 2 * self.min_val - top_val
        if not self.stack:
            self.min_val = None

    def top(self) -> int:
        if not self.stack:
            return None
        
        top_val = self.stack[-1]
        if top_val < self.min_val:
            return self.min_val
        return top_val
        
    def getMin(self) -> int:
        return self.min_val
