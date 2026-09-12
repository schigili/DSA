from bisect import bisect_right
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = [(s, e, w, i) for i, (s, e, w) in enumerate(intervals)]
        arr.sort(key=lambda x: x[0])
        start_times = [x[0] for x in arr]
        
        dp = [[(0, ())] * 5 for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            s, e, w, orig_idx = arr[i]
            j = bisect_right(start_times, e)
            
            for k in range(1, 5):
                opt1 = dp[i + 1][k]
                
                prev_w, prev_indices = dp[j][k - 1]
                new_w = w + prev_w
                new_indices = tuple(sorted(prev_indices + (-orig_idx,), reverse=True))
                opt2 = (new_w, new_indices)
                
                dp[i][k] = opt1 if opt1 > opt2 else opt2
                
        best_w, best_neg_indices = dp[0][4]
        
        return [-x for x in best_neg_indices]