from collections import OrderedDict

class LRUCache:
    
    def __init__(self,capacity:int) -> None:
        self.order_dict = OrderedDict()
        self.capacity = capacity

    def get(self, key:int) -> int:
        for i in self.order_dict:
            if i == key:
                self.order_dict.move_to_end(key,last = False)
                return self.order_dict[i]
        return -1
    
    def put(self,key:int,value:int ) -> None:
        if key not in self.order_dict and len(self.order_dict) >= self.capacity:
            self.order_dict.popitem(last=True)
        self.order_dict[key] = value
        self.order_dict.move_to_end(key,last=False)

lRUCache =LRUCache(2)
lRUCache.put(1, 1)
print(lRUCache.order_dict)
lRUCache.put(2, 2)
print(lRUCache.order_dict)
lRUCache.get(1)
print(lRUCache.order_dict)
lRUCache.put(3, 3)
print(lRUCache.order_dict)
lRUCache.get(2)
print(lRUCache.order_dict)
lRUCache.put(4, 4)
print(lRUCache.order_dict)
lRUCache.get(1)
print(lRUCache.order_dict)
lRUCache.get(3)
print(lRUCache.order_dict)
lRUCache.get(4)
print(lRUCache.order_dict)
