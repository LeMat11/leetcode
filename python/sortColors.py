
# def sortColors(nums):
#     left = 0
#     right = len(nums) -1
#     mid = 0
#     while left < right and mid < len(nums):
#         while mid < len(nums) and nums[mid] == 1:
#             mid += 1
#         while nums[left]== 0 and left<right: 
#             left += 1
#         while nums[right] == 2 and left<right:
#             right -= 1
#         if nums[left] == 1:
#             temp = nums[left]
#             nums[left] = nums[mid]
#             nums[mid] = temp
#         if nums[left] > nums[right]:
#             temp = nums[left]
#             nums[left] = nums [right]
#             nums[right] = temp
#             while nums[left] == 0: left +=1
#             while nums[right] == 2 : right-=1
#             if nums[left] == nums[right]:
#                 break
#         if mid == len(nums):
#             break
#     return nums

def sortColors(nums):
    red, white, blue = 0, 0, len(nums)-1
    while white <= blue:
        if nums[white] == 0:
            nums[red], nums[white] = nums[white], nums[red]
            red +=1
            white +=1
        elif nums[white] == 1:
            white += 1
        else:
            nums[blue],nums[white] = nums[white],nums[blue]
            blue -= 1
    return nums

def main():
    nums = [1,0,1]
    res = sortColors(nums)
    print(res)

main()