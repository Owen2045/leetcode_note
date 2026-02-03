from typing import Optional, List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        end = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[end-1]:
                nums[end] = nums[i]
                end += 1
        return end