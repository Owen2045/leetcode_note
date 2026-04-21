from typing import List
from collections import Counter
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)        
        
def print_list(node):
    while node:
        print(node.val, end=" → ")
        node = node.next
    print("None")        

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head        
        
        next_node = curr.next
        print(next_node)
        
# head = [1,2,3,4,5]
# a = Solution()
# a.reverseList(head)