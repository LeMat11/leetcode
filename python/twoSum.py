from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []  

def main():
    nums = [2,7,11,15]
    target = 18
    solution = Solution()
    result = solution.twoSum(nums,target)
    print(result)

main()