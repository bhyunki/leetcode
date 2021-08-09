class MyStack:
    my_list = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.my_list = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.my_list.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.my_list.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.my_list[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.my_list

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
