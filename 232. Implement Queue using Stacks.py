class MyQueue:

    def __init__(self):
        self.q = []     # end | 3 2 1 | front
        self.tmp = []   # 

    def push(self, x: int) -> None: # add to the back of the queue.
        while self.q:
            self.tmp.append(self.q.pop())
        self.q.append(x)
        while self.tmp:
            self.q.append(self.tmp.pop())
        return

    def pop(self) -> int:
        return self.q.pop()

    def peek(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        if not self.q: return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()