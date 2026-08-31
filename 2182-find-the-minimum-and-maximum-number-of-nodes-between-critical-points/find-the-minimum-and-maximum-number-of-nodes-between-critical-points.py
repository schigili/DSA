
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        first_crit_idx = -1
        prev_crit_idx = -1
        min_dist = float('inf')
        
        prev = head
        curr = head.next
        idx = 1
        
        while curr.next:
            nxt = curr.next
            
            if (curr.val > prev.val and curr.val > nxt.val) or (curr.val < prev.val and curr.val < nxt.val):
                if first_crit_idx == -1:
                    first_crit_idx = idx
                else:
                    min_dist = min(min_dist, idx - prev_crit_idx)
                
                prev_crit_idx = idx
            
            prev = curr
            curr = nxt
            idx += 1
            
        if min_dist == float('inf'):
            return [-1, -1]
        
        max_dist = prev_crit_idx - first_crit_idx
        
        return [min_dist, max_dist]