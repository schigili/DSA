class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        fst, lst = {}, {}
        for i, c in enumerate(s):
            fst.setdefault(c, i)
            lst[c] = i
        
        intervals = []
        for c in fst:
            start, end = fst[c], lst[c]
            i, valid = start, True
            while i <= end:
                if fst[s[i]] < start:
                    valid = False
                    break
                end = max(end, lst[s[i]])
                i += 1
            if valid:
                intervals.append((end, start))
                
        intervals.sort()
        ans, prev = [], -1
        for end, start in intervals:
            if start > prev:
                ans.append(s[start:end+1])
                prev = end
        return ans