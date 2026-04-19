from typing import List
from collections import Counter

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        # 塞一個正序
        self.s1.append(x)

    def pop(self) -> int:
        # 移除並回傳 queue 最前端的元素
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2.pop()

    def peek(self) -> int:
        # 回傳 queue 最前端的元素（不移除
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2
        # 回傳 queue 是否為空


# Your MyQueue object will be instantiated and called as such:

obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
print(param_2)
param_3 = obj.peek()
print(param_3)
param_4 = obj.empty()
print(param_4)


