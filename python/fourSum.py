def foursum(nums,target):
    res = set()
    nums.sort()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)-2):
            left = j+1
            right = len(nums)-1
            while left < right:
                sum = nums[i] + nums[j] + nums[left] + nums[right]
                if sum < target:
                    left += 1 
                if sum > target:
                    right -= 1 
                elif sum == target:
                    res.add(tuple((nums[i],nums[j],nums[left],nums[right])))
                    left += 1
                    right -= 1
    return res

def main():
    nums = [1,-2,-5,-4,-3,3,3,5]
    target = -11
    a = foursum(nums,target)
    print(a)

main()