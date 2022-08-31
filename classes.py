class Stack:

    def __init__(self):
        self.information = []

    def isEmpty(self):
        return self.information == []

    def push(self, information):
        self.information.append(information)

    def pop(self):
        result = self.information.pop()
        return result

    def peek(self):
        return self.information[-1]

    def size(self):
        return len(self.information)

