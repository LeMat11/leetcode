from collections import deque
class Stack:
    def __init__(self) -> None:
        self.stack = deque()

    def push(self,val:int) -> None:
        self.stack.append(val)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
    
class MyQueue:
    def __init__(self) -> None:
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self,val:int) -> None:
        self.stack1.append(val)

    def pop(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.push(self.stack1.pop())
            return self.stack2.pop()
        
    def peek(self) -> int:
        if self.stack2:
            return self.stack2[1]
        else:
            while self.stack1:
                self.stack2.push(self.stack1.pop())
            return self.stack2[1]
        
    def isempty(self) -> bool:
        return not self.stack1 and not self.stack2
            