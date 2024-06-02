def removeElement(nums,val):
    fast = 0
    slow = 0
    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow +=1
        fast += 1
    return slow

def main():
    nums = [3,2,2,3]
    val = 3
    removeElement(nums,val)

main()