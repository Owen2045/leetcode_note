from typing import List

class Solution:
    def isPalindrome(self, p: int) -> bool:
        f = 0
        x = p
        while x >= 1:
            b = x % 10
            x = x // 10
            f = f * 10 + b
            # print(f)
            
        print(p, f)
        return p == f

a = Solution()
print(a.isPalindrome(121))

