from typing import Optional, List

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        l = s.split(" ")
        for i in l[::-1]:
            if i:
                return len(i)
            
        