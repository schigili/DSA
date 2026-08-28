from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s, target):
        count = Counter(s)
        n = len(s)
        
        
        odd_chars = [char for char, freq in count.items() if freq % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        
        
        half_s = Counter({char: freq // 2 for char, freq in count.items()})
        m = n // 2
        
        
        target_half_count = Counter(target[:m])
        if all(half_s[c] == target_half_count[c] for c in half_s):
            candidate_p = target[:m] + mid_char + target[:m][::-1]
            if candidate_p > target:
                return candidate_p
                
        
        for i in range(m - 1, -1, -1):
            pref_count = Counter(target[:i])
            
            
            if all(half_s[c] >= pref_count[c] for c in pref_count):
                rem_count = half_s - pref_count
                
                
                target_char = target[i]
                best_char = None
                
                for c in sorted(rem_count.keys()):
                    if c > target_char and rem_count[c] > 0:
                        best_char = c
                        break
                        
                
                if best_char:
                    rem_count[best_char] -= 1
                    
                    
                    rem_chars = []
                    for c, cnt in rem_count.items():
                        rem_chars.extend([c] * cnt)
                    rem_chars.sort()
                    
                    first_half = target[:i] + best_char + "".join(rem_chars)
                    return first_half + mid_char + first_half[::-1]
                    
        return ""