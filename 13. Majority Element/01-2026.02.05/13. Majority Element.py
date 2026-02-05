class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        main = 0
        
        for i in nums:
            if c == 0:
                main = i
                
            print(c, main)
            
            if i != main:
                c -= 1
            else:
                c += 1
