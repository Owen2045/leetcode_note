class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_boundary = 0
        

        for i in range(len(nums)):
            if i > max_boundary:
                return False
            
            max_boundary = max(max_boundary, i+nums[i])
            if max_boundary >= len(nums)-1:
                return True
            
        return True
