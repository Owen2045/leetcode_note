from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start_sum = sum(nums[0:k])

        ans = start_sum



        for i in range(len(nums)):
            end = i + k
            if end >= len(nums):
                break
            
            start_sum += nums[end]
            start_sum -= nums[i]
            if start_sum > ans:
                ans = start_sum

        return ans / k

