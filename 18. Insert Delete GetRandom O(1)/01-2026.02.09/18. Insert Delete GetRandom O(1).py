from typing import Optional, List
import time
import random

class RandomizedSet:

    def __init__(self):
        self.data_list = []
        self.data_map = {}

    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False        
        else:
            self.data_map[val] = len(self.data_list)
            self.data_list.append(val)
            
            print(self.data_map)
            print(self.data_list)
            
            return True

    def remove(self, val: int) -> bool:
        if val in self.data_map:
            idx = self.data_map.get(val)
            last_val = self.data_list[-1]
            self.data_map[last_val] = idx
            self.data_list[idx] = self.data_list[-1]
            del self.data_map[val]
            self.data_list.pop()
            return True
        else:
            return False
        
        
    def getRandom(self) -> int:
        return random.choice(self.data_list)

obj = RandomizedSet()
for i in [1, 0, 3, 5, 8, 6, 4]:
    
    param_1 = obj.insert(i)
    

param_2 = obj.remove(5)

param_3 = obj.getRandom()
print(param_3)