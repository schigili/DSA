class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        min_len = [float('inf')] * n
        left = 0
        current_sum = 0
        ans = float('inf')
        best_so_far = float('inf')

        for right in range(n):
            current_sum += arr[right]
            
            while current_sum > target:
                current_sum -= arr[left]
                left += 1
            
            if current_sum == target:
                length = right - left + 1
                if left > 0 and min_len[left - 1] != float('inf'):
                    ans = min(ans, length + min_len[left - 1])
                best_so_far = min(best_so_far, length)
            
            min_len[right] = best_so_far

        return ans if ans != float('inf') else -1