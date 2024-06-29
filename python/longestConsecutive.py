from typing import List
from ListNode import ListNode

def longestConsecutive(nums:List[int]) -> int:
    nums = set(nums)
    maxval = 0
    for num in nums:
        if num-1 not in nums:
            curr_num = num
            val = 1
            while curr_num+1 in nums:
                curr_num += 1
                val += 1 
            maxval = max(maxval,val)
    return maxval

nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums)) 