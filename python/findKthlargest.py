import heapq as hq
import random 
def findKthLargest(nums,k):
    #method 1
    h = list()
    for num in nums:
        hq.heappush(h,num)
        if len(h) > k:
            hq.heappop(h)
    return hq.heappop(h)
    
    #method 2
def partition(list,left,right):
    pivot_index = random.randint(left,right)
    pivot_value = list[pivot_index]
    list[pivot_index], list[right] = list[right], list[pivot_index]
    store_index = left
    for i in list:
        if list[i] < pivot_value:
            list[i], list[store_index] = list[store_index], list[i]
            store_index +=1
    list[store_index], list[right] = list[right],list[store_index]
    return store_index

def quickselect(nums,left, right,k):
    if left == right:
        return nums[left]
    pivot_index = partition(nums,left,right)
    if pivot_index == k:
        return nums[pivot_index]
    elif pivot_index < k:
        return quickselect(nums,left,pivot_index-1,k)
    else: return quickselect(nums,pivot_index+1,right,k)
    


def main():
    nums = [1,2,4,6,7,4,2,5]
    k = 4
    ans = findKthLargest(nums,k)
    print(ans)

main()