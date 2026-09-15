class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        isPal = [[False] * n for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 2:
                        isPal[i][j] = True
                    else:
                        isPal[i][j] = isPal[i+1][j-1]
                        
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            dp[i] = dp[i-1]
            for j in range(i - k + 1):
                if isPal[j][i-1]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        return dp[n]