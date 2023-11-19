class MyNode:
    def __init__(self, key=None):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.hash = [MyNode() for _ in range(10 ** 4)]
    
    # hash function
    def hashfunc(self, key):
        unicode_sum = 0
        for ch in str(key):
            unicode_sum += ord(ch)
        return unicode_sum % (10 ** 3)

    def add(self, key: int) -> None:        
        i = self.hashfunc(key)
        curr = self.hash[i]
        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next
        curr.next = MyNode(key)

    def remove(self, key: int) -> None:
        i = self.hashfunc(key)
        curr = self.hash[i]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        i = self.hashfunc(key)
        curr = self.hash[i]
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        return False