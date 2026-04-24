from typing import List
from collections import Counter
from typing import Optional



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 上一個節點
        prev = None
        # 當前節點
        curr = head
        # 當前節點不為空的時候
        while curr is not None:
            # 先存當前的下一個節點
            next_node = curr.next
            # 下一個指給上一個節點
            curr.next = prev
            # 上一個節點前進到當前節點
            prev = curr
            # 當前節點前進到下個節點
            curr = next_node
        # 當前節點為空的時候 上一個節點就是新的頭了
        return prev
        
        
vals = [1, 2, 3, 4, 5]
head = ListNode(vals[0])
curr = head
for v in vals[1:]:
    curr.next = ListNode(v)
    curr = curr.next


a = Solution()
b = a.reverseList(head)
print(b)

