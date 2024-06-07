import heapq as hq
def findKthLargest(nums,k):
    #method 1
    h = list()
    for num in nums:
        hq.heappush(h,num)
        if len(h) > k:
            hq.heappop(h)
    return hq.heappop(h)
    
    #method 2
    

def main():
    nums = [1,2,4,6,7,4,2,5]
    k = 4
    ans = findKthLargest(nums,k)
    print(ans)

main()