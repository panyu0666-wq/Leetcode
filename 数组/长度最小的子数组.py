# 滑动窗口法：有一个左指针和一个右指针，右指针负责不断扩大窗口，左指针负责缩小窗口以满足限制要求
nums = list(map(int,input().split(" ")))
s = int(input())
def minSubArrayLen(s: int, nums: list[int]) -> int:
    left = 0
    sum = 0
    ans = float("inf")
    for right in range(len(nums)):
        # 窗口开始扩大
        sum += nums[right]
        # 当窗口大小满足要求时，尝试缩小窗口
        while sum >= s:
            ans = min(ans, right - left + 1)
            sum -= nums[left]
            left += 1
    if ans == float("inf"):
        return 0
    return ans
ans = minSubArrayLen(s, nums)
print(ans)