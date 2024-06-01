def threeSum(nums):
    res = set()
    nums.sort()
    for i in range(len(nums)):  
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i+1
        right = len(nums)-1
        while left < right:
            sum =  nums[i] + nums[left] + nums [right];
            if sum > 0: right-=1
            if sum < 0: left+=1
            elif sum==0:
                res.add(tuple((nums[i],nums[left],nums[right])))
                left += 1
                right -= 1
    return res

def main():
    a = threeSum([-1,0,1,2,-1,-4])
    print(a)    
                
main()
