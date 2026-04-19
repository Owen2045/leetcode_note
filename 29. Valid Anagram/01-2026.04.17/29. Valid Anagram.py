from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        ss = sorted(s)
        tt = sorted(t)
        if len(ss) != len(tt):
            return False
        for j, k in zip(ss, tt):
            if j != k:
                return False
        return True





s = "anagram"
t = "nagaram"
a = Solution()
b = a.isAnagram(s, t)
print(b)





