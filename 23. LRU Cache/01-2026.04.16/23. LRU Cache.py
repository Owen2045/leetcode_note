from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.max_cache_len = capacity
        self.cache_dict = OrderedDict()
        return None
        
        

    def get(self, key: int) -> int:
        if key in self.cache_dict:
            self.cache_dict.move_to_end(key)
            return self.cache_dict.get(key)
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.cache_dict[key] = value
        self.cache_dict.move_to_end(key)
        if len(self.cache_dict) > self.max_cache_len:
            self.cache_dict.popitem(last=False)

