class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.nodeMap = {}
        self.capacity = capacity

        self.right = ListNode(-1, -1)
        self.left = ListNode(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left
    #     self.cache = OrderedDict()
    #     self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        
        node = self.nodeMap[key]
        self.remove(node)
        self.insert(node)
        return node.val
        
    #     if key not in self.cache:
    #         return -1
    #     self.cache.move_to_end(key)
    #     return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            self.remove(self.nodeMap[key])
        
        node = ListNode(key, value)
        self.insert(node)
        self.nodeMap[key] = node

        if len(self.nodeMap) > self.capacity:
            node = self.left.next
            self.remove(node)
            del self.nodeMap[node.key]
    #     if key in self.cache:
    #         self.cache.move_to_end(key)
    #     self.cache[key] = value

    #     if len(self.cache) > self.cap:
    #         self.cache.popitem(last=False)

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.next = nxt
        node.prev = prev
        nxt.prev = node
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev