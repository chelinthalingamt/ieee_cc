class MinMaxStack:
    def __init__(self):
        self.stack = []  
        self.min_stack = []  
        self.max_stack = [] 

    def push(self, x):
      """"Pushes element x onto the stack."""
        self.stack.append(x)
        
        # Update min stack
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])
        
        # Update max stack
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        """Removes the top element from the stack."""
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
            self.max_stack.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def top(self):
        """Returns the top element without removing it."""
        if self.stack:
            return self.stack[-1]
        raise IndexError("Stack is empty")

    def getMin(self):
        """Returns the smallest element in the stack."""
        if self.min_stack:
            return self.min_stack[-1]
        raise IndexError("Stack is empty")

    def getMax(self):
        """Returns the largest element in the stack."""
        if self.max_stack:
            return self.max_stack[-1]
        raise IndexError("Stack is empty")

# Example Usage:
stack = MinMaxStack()
stack.push(5)
stack.push(3)
stack.push(8)
stack.push(2)

print(stack.getMin())  # Output: 2
print(stack.getMax())  # Output: 8
print(stack.top())     # Output: 2

stack.pop()
print(stack.getMin())  # Output: 3
print(stack.getMax())  # Output: 8
