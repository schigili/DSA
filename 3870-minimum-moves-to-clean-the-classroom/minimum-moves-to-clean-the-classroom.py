from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        start_r = start_c = -1
        litter_coords = []
        
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter_coords.append((r, c))
                    
        num_litter = len(litter_coords)
        if num_litter == 0:
            return 0
            
        litter_idx = {coord: i for i, coord in enumerate(litter_coords)}
        
       
        visited = [[[-1] * (1 << num_litter) for _ in range(n)] for _ in range(m)]
        visited[start_r][start_c][0] = energy
        
        q = deque([(0, start_r, start_c, 0, energy)])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        target_mask = (1 << num_litter) - 1
        
        while q:
            moves, r, c, mask, e = q.popleft()
            
            if mask == target_mask:
                return moves
                
            if e == 0:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    nmask = mask
                    ne = e - 1
                    
                    if classroom[nr][nc] == 'L':
                        idx = litter_idx[(nr, nc)]
                        nmask |= (1 << idx)
                        
                    if classroom[nr][nc] == 'R':
                        ne = energy
                        
                    if ne > visited[nr][nc][nmask]:
                        visited[nr][nc][nmask] = ne
                        q.append((moves + 1, nr, nc, nmask, ne))
                        
        return -1