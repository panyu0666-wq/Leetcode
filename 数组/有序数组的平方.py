# 双指针法
# 首先数组是有序的，那么最大的元素一定在数组的首部或末尾，所以定义慢指针在首部，快指针在末尾，然后一起往中间走，然后新数组从尾部开始加
nums = list(map(int,input().split(" ")))
def sortedSquares(nums:list[int]):
    slow,fast = 0,len(nums)-1
    new_nums = [0]*len(nums)
    k = len(nums)-1
    while slow <= fast:
        if nums[slow]**2 > nums[fast]**2:
            new_nums[k] = nums[slow]**2
            slow += 1
            k -= 1
        else:
            new_nums[k] = nums[fast]**2
            fast -= 1
            k -= 1
    return new_nums
ans = sortedSquares(nums)
print(ans)