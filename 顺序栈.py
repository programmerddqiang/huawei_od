class Stack:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push(self,item):
        self.elems.append(item)

    def destack(self):
        if self.is_empty():
            raise Exception()
        return self.elems.pop()