nums = list(map(int,input().split(" ")))
target = int(input())
def search(nums:list[int], target:int):
    left, right = 0, len(nums)-1
    while left <= right:
        middle = (left + right)//2
        if nums[middle] > target:
            right = middle-1
        elif nums[middle] < target:
            left = middle + 1
        else:
            return middle
    return -1
ans = search(nums,target)
print(ans)