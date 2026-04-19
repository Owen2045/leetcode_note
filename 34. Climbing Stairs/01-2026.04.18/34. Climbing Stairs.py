from typing import List
from collections import Counter


class Solution:
    def climbStairs(self, n: int) -> int:
        # 費氏數列0 1 1 2 3 5 8
        
        if n == 1:
            return 1
        
        if n == 2:
            return 2

        # 先做儲存清單 [0, 0, 0, 0, 0]
        dp = [0] * (n + 1)

        dp[1] = 1
        dp[2] = 2
        


        # 再用迴圈填數字
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]

n = 2

a = Solution()
b = a.climbStairs(n)
print(b)

