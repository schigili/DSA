from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        
        idx1 = min(min_idx, max_idx)
        idx2 = max(min_idx, max_idx)
        
        front_deletions = idx2 + 1
        back_deletions = n - idx1
        mixed_deletions = (idx1 + 1) + (n - idx2)
        
        return min(front_deletions, back_deletions, mixed_deletions)