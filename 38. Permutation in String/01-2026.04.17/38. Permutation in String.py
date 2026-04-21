from typing import List
from collections import Counter
import heapq

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = len(s1)
        start = 0
        s_count = Counter(s1)
        v_count = Counter(s2[start:len(s1)])
        if v_count == s_count:
            return True
        
        for end in range(a, len(s2)):
                
            v_count[s2[end]] += 1
            
            v_count[s2[end-a]] -= 1
            
            if v_count[s2[end-a]] == 0:
                del v_count[s2[end-a]]
            if v_count == s_count:
                return True
        return False

        


# Your MinStack object will be instantiated and called as such:


