from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = {}
        for i in nums:
            if i in ans:
                ans[i] += 1
            else:
                ans[i] = 1
        print(ans)
        output = []

        
        for n, f in ans.items():
            heapq.heappush(output, (f, n))
            if len(output) > k:
                heapq.heappop(output)
        print(output)
        return [x[1] for x in output]



nums = [1,1,1,2,2,3]
k = 2


a = Solution()
b = a.topKFrequent(nums, k)
print(b)