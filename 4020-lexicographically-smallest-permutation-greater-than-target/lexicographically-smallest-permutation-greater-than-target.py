from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s, target):
        s_count = Counter(s)
        n = len(s)
        
        for i in range(n - 1, -1, -1):
            pref_count = Counter(target[:i])
            
            if all(s_count[c] >= pref_count[c] for c in pref_count):
                rem_count = s_count - pref_count
                
                target_char = target[i]
                best_char = None
                
                for c in sorted(rem_count.keys()):
                    if c > target_char and rem_count[c] > 0:
                        best_char = c
                        break
                        
                if best_char:
                    rem_count[best_char] -= 1
                    
                   
                    rem_chars = []
                    for c, count in rem_count.items():
                        rem_chars.extend([c] * count)
                    rem_chars.sort()
                    
                    return target[:i] + best_char + "".join(rem_chars)
                    
        return ""