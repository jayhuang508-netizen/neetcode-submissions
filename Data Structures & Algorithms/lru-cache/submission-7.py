
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.volumn = 0

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left
    
    # to get less complexity, define the assist functions
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next= nxt
        nxt.prev = prev
    
    def insert(self, node):
        # insert the new node into the end
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # if duplicate
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        # self.volumn += 1
        if len(self.cache)> self.cap:
            head = self.left.next
            self.remove(head)
            del self.cache[head.key]
            # self.volumn -= 1
        
