class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        last = {}
        
        for i, char in enumerate(s):
            dp[i + 1] = (2 * dp[i]) % MOD
            if char in last:
                dp[i + 1] = (dp[i + 1] - dp[last[char] - 1]) % MOD
            last[char] = i + 1
            
        return (dp[-1] - 1) % MOD