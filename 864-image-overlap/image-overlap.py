import collections
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ones1 = []
        ones2 = []
        
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    ones1.append((i, j))
                if img2[i][j] == 1:
                    ones2.append((i, j))
                    
        if not ones1 or not ones2:
            return 0
            
        t_counts = collections.defaultdict(int)
        ans = 0
        
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                t = (r2 - r1, c2 - c1)
                t_counts[t] += 1
                if t_counts[t] > ans:
                    ans = t_counts[t]
                    
        return ans