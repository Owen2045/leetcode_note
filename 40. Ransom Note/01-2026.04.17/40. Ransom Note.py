from typing import List
from collections import Counter
import heapq

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = Counter(magazine)
        for i in ransomNote:
            val = dic.get(i)
            if not val:
                return False
            val -= 1
            dic[i] = val
            if val < 0:
                return False
        return True
        