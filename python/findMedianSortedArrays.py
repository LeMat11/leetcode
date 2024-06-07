def findMedianSortedArrays(nums1,nums2):
    nums = nums1 + nums2
    nums.sort()
    n = len(nums)
    if n % 2:
        res = nums[int((n - 1)/2)]
        return "{:.5f}".format(res)
    else: 
        res = (nums[int(n/2)]+nums[int(n/2-1)])/2
        return "{:.5f}".format(res)
    
def main():
    nums1 = [1,2]
    nums2 = [3,4]
    ans = findMedianSortedArrays(nums1 , nums2)
    print(ans)

main()