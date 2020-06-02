class Stack:

    def __init__(self):
        self.list = []

    def push(self, data):
        self.list.append(data)

    def pop(self):
        return self.list.pop()

    def print_list(self):
        return self.list


s = Stack()
s.push('A')
s.push('B')
s.push('C')
print(s.print_list())
s.pop()
print(s.print_list())