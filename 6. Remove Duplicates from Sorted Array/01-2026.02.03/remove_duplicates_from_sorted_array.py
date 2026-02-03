from typing import Optional, List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nt = 0

        while True:
            now_len = len(nums)
            next_nt = nt + 1
            if nt >= now_len or next_nt >= now_len:
                break
            
            if nums[nt] == nums[next_nt]:
                nums.pop(next_nt)
            else:
                nt +=1
        return len(nums)
            
            
            
