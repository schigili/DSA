from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
            
        sorted_nums = sorted([(nums[i], i) for i in range(n)])
        res = [0] * n
        
        group_vals = []
        group_idx = []
        
        for i in range(n):
            if not group_vals:
                group_vals.append(sorted_nums[i][0])
                group_idx.append(sorted_nums[i][1])
            else:
                if sorted_nums[i][0] - group_vals[-1] <= limit:
                    group_vals.append(sorted_nums[i][0])
                    group_idx.append(sorted_nums[i][1])
                else:
                    group_idx.sort()
                    for j in range(len(group_idx)):
                        res[group_idx[j]] = group_vals[j]
                        
                    group_vals = [sorted_nums[i][0]]
                    group_idx = [sorted_nums[i][1]]
                    
        if group_vals:
            group_idx.sort()
            for j in range(len(group_idx)):
                res[group_idx[j]] = group_vals[j]
                
        return res