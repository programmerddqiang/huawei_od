class solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, item):
        self.stack1.append(item)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        if not self.stack1:
            raise Exception("pop from empty queue")
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
