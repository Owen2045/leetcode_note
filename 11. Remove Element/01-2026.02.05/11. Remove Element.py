from typing import Optional, List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0

        for _ in range(len(nums)):
            if nums[j] == val:
                nums.append(nums[j])
                nums.pop(j)
            else:
                j += 1
        return j
        
