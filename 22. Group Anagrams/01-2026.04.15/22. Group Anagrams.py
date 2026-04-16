from typing import Optional, List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        record = {}
        for i in range(len(nums)):
            if nums[i] in record:
                return True
            else:
                record[nums[i]] = i
        return False
        
