def largestNumber(nums):
    nums = list(map(str,nums))
    res = list(str())
    i = 0
    while nums:
        nums = sorted(nums[i:],key=lambda x:x[i],reverse=True)
        res.append(nums[i])
    ans = "".join(res) 
    return ans

def main():
    nums = [3,30,34,5,9]
    res = largestNumber(nums)
    print (res)

main()
    