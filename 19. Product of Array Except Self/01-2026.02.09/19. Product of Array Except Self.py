from typing import Optional, List
import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = []
        ans_map = {}
        
        for i in range(len(nums)):
            
            if ans_map.get(nums[i]):
                ans.append(ans_map.get(nums[i]))
            else:
                left = math.prod(nums[0:i])
                right = math.prod(nums[i+1:])
                x = left*right
                ans.append(x)
                ans_map[nums[i]] = x

        return ans