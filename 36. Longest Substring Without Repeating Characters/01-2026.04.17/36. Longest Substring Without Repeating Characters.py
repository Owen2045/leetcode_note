from typing import List
from collections import Counter
from typing import Optional



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        ans = set()
        max_len = 0
        for i in range(len(s)):
            while s[i] in ans:
                ans.remove(s[start])
                start += 1
            ans.add(s[i])
            max_len = max(max_len, (i-start+1))
        return max_len                
        
        
        
s = "pwwkewwwww"
a = Solution()
b = a.lengthOfLongestSubstring(s)
print(b)

