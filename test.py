from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:

        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]



# heapify	init 時把 nums 轉成 heap
# heappush	add 時推入新值
# heappop	超過 k 個時把最小的踢掉


a = KthLargest(3, [4, 5, 8, 2])
print(a.add(3))
print(a.add(5))
print(a.add(10))