from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        a = Counter(s)

        result = ""

        for ch, count in sorted(a.items(), key=lambda x: x[1], reverse=True):
            result += ch * count

        return result
        
