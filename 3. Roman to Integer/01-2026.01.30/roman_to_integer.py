from typing import List


class Solution:
    def romanToInt(self, s: str) -> int:
        rm_map = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        ans = 0
        now_num = 0
        for o in reversed(s):
            i = rm_map[o]
            if i < now_num:
                ans -= i
            else:
                ans += i
            now_num = i

        return ans
