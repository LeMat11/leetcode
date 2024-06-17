from collections import deque


class MinStack:

    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
    
def main():
    m = MinStack()
    m.push(-3)
    m.push(3)
    m.push(2)
    print(m.top())
    print(m.getMin())
    m.pop()
    m.pop()
    m.pop()
    print(m.top())

main()