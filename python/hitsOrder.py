from collections import deque


class hitOrder:
    def __init__(self) -> None:
        self.hits = deque()

    def hit(self,timestamp:int):
        self.hits.append(timestamp)

    def getHits(self,timestamp:int):
        while self.hits and self.hits[0] <= timestamp -300:
            self.hits.popleft()
        return len(self.hits)