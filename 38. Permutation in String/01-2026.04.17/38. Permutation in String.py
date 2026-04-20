from typing import List
from collections import Counter
import heapq

class MinStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, val: int) -> None:
        # pushes the element val onto the stack.
        self.s1.append(val)
        if self.s2:
            if self.s2[-1] > val:
                self.s2.append(val)
            else:
                self.s2.append(self.s2[-1])
        elif not self.s2:
            self.s2.append(val)

    def pop(self) -> None:
        self.s1.pop()
        self.s2.pop()

    def top(self) -> int:
        return self.s1[-1]

    def getMin(self) -> int:
        return self.s2[-1]
        


# Your MinStack object will be instantiated and called as such:

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)

print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin()) 

