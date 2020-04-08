import sys

input = sys.stdin.readline
command_count = int(input())
stack = []

def command_processor(command_input):
    command = command_input.split()[0]
    if len(command_input.split())>1:
        num = command_input.split()[1]

    if command == 'push':
        stack.append(num)
    elif command == 'pop':
        if len(stack):
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif command == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
for i in range(command_count):
    command_processor(input())
