from typing import List
from collections import Counter

class MyQueue:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char = set()
        left = 0
        ans = 0

        for right in range(len(s)):

            while s[right] in char:
                char.remove(s[left])
                left += 1

            char.add(s[right])
            ans = max(ans, right - left +1)
        return ans
    

s = "bbbbb"
a = MyQueue()
b = a.lengthOfLongestSubstring(s)
print(b)
