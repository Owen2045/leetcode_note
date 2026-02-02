from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        ans_list = []
        for af in strs:
            f_idx = None
            for i, st in enumerate(shortest):
                if af[i] == st:
                    f_idx = i
                else:
                    break
            ans_list.append(f_idx)
            
        if None in ans_list:
            return ""
        else:
            return shortest[:min(ans_list)+1]
