class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        min_length=float('inf')
        window_sum=0
        for right in range(len(nums)):
            window_sum=window_sum+nums[right]
            while window_sum>=target:
                min_length=min(min_length,(right-left+1))
                window_sum=window_sum-nums[left]
                left=left+1
        if min_length==float('inf'):
            return 0
        else:
            return min_length