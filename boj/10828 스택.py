class Stack:
    def __init__(self):
        self.len = 0
        self.list =[]
    #push
    def push(self, num):
        self.list.append(num)
        self.len += 1
    #pop
    def pop(self):
        if self.size() == 0:
            return -1
        pop_result = self.list[self.len-1]
        del self.list[self.len-1]
        self.len -= 1
        return pop_result
    #size
    def size(self):
        return self.len
    #empty
    def empty(self):
        if self.len == 0:
            return 1
        else:
            return 0
    #top
    def top(self):
        if self.size() != 0:
            return self.list[-1]
        else:
            return -1

num = int(input())
stack = Stack()
while num > 0:
    num -= 1
    input_split = input().split()

    op = input_split[0]
    if op == 'push':
        stack.push(input_split[1])
    elif op == 'pop':
        print(stack.pop())
    elif op == 'size':
        print(stack.size())
    elif op == 'empty':
        print(stack.empty())
    elif op == 'top':
        print(stack.top())
    else:
        print('Error')