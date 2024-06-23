from collections import deque

class MovingAverage:
    def __init__(self,size:int) -> None:
        self.size = size
        self.q = deque()
        self.sum = 0

    def next(self,val:int) -> float:
        self.q.append(val)
        self.sum += val
        if len(self.q) > self.size:
            self.sum -= self.q.popleft()
        return self.sum/len(self.q)
    
moving_average = MovingAverage(3)
print(moving_average.next(1))  # Output: 1.0
print(moving_average.next(10)) # Output: 5.5
print(moving_average.next(3))  # Output: 4.67
print(moving_average.next(5))