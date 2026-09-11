class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        counts = [0] * 10
        for d in digits:
            counts[d] += 1
            
        ans = 0
        for num in range(100, 1000, 2):
            curr = [0] * 10
            curr[num % 10] += 1
            curr[(num // 10) % 10] += 1
            curr[num // 100] += 1
            
            if all(curr[i] <= counts[i] for i in range(10)):
                ans += 1
                
        return ans