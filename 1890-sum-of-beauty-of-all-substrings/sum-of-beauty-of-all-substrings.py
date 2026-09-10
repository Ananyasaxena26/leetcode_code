from collections import Counter
class Solution:
    def beautySum(self, s: str) -> int:
        sum=0
        for j in range(len(s)):
            for i in range(j+1):
                l=s[i:j+1]
                freq=dict(Counter(l))
                
                max_val = max(freq.values())
                min_val = min(freq.values())
                sum+=max_val-min_val
        return sum