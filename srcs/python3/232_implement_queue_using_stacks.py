class MyQueue:
    my_q = None
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.my_q=[]

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.my_q.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.my_q.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.my_q[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.my_q


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
