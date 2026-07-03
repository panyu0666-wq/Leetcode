# 双指针法：使用一个快指针和一个慢指针在一个for循环中完成两个for循环的功能
nums = list(map(int,input().split(" ")))
val = int(input())
# 快指针：用来遍历数组，查找不含目标值的元素
# 慢指针：用来记录不含目标值的元素的位置
def removeElement(nums:list[int], val:int):
    slow,fast = 0,0
    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow
ans = removeElement(nums,val)
print(ans)
    