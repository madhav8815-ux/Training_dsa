class Node:
    def __init__(self, data = None):
        self.value = data
        self.next = None

class MyQueue:

    def __init__(self):
        self.start = self.end = None

    def push(self, x: int) -> None:
        temp = Node(x)
        if self.start == None:
            self.start = self.end = temp
        else :
            self.end.next = temp
            self.end = temp

    def pop(self) -> int:
        data = self.start.value
        if self.start.next == None:
            self.start = self.end = None
        else:
            self.start = self.start.next
        return data

    def peek(self) -> int:
        return self.start.value

    def empty(self) -> bool:
        return (self.start == None and self.end == None)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()