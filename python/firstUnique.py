from typing import Counter, List,Optional


class FirstUnique:
    def __init__(self,nums:List[int]) -> None:
        self.nums = nums
        self.counter = Counter(nums)
        
    def showFirst(self) -> Optional[int]:
        for num in self.nums:
            if self.counter[num] == 1:
                return num
        return None
    
    def add(self, num:int) -> None:
        self.nums.append(int)
        self.counter[num] += 1
    
def main():
    test_cases = [2,3,5]
    FN = FirstUnique(test_cases) 
    print(FN.showFirst())
    FN.add(2)
    print(FN.showFirst())
    FN.add(3)
    print(FN.showFirst())
    FN.add(5)
    print(FN.showFirst)

main()