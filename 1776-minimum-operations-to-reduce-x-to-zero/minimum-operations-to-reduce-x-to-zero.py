class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0: return -1
        
        max_len, current_sum, left = -1, 0, 0
        for right, val in enumerate(nums):
            current_sum += val
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
                
        return len(nums) - max_len if max_len != -1 else -1