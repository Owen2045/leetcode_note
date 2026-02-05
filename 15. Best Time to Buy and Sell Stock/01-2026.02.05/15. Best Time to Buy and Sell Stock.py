class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        min_price = nums[0]
        max_money = 0
        for i in range(1, len(nums)):
            if nums[i] < min_price:
                min_price = nums[i]
            
            now_price = nums[i] - min_price
            if now_price > max_money:
                max_money = now_price
        return max_money
