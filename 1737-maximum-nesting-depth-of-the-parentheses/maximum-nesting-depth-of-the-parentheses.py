class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        curr = 0
        for char in s:
            if char == '(':
                curr += 1
                if curr > ans:
                    ans = curr
            elif char == ')':
                curr -= 1
        return ans