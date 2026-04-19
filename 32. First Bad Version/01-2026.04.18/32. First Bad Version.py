from typing import List
from collections import Counter
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        s = 0
        

        while n >= s:
            mid = (s + n) // 2
            print(mid)

            if isBadVersion(mid):
                n = mid -1

            else:
                s = mid + 1
        return s


def isBadVersion(version: int) -> bool:
    bad = 4
    return version >= bad   # bad 之後全是壞的



n = 5
bad = 4
a = Solution()
b = a.firstBadVersion(n)
print(b)