import sys
from collections import deque

input = sys.stdin.readline
command_count = int(input())
dq = deque()

def command_processor(command_input):
    command = command_input.split()[0]
    if len(command_input.split()) > 1:
        num = command_input.split()[1]

    if command == 'push':
        dq.append(num)

    elif command == 'front':
       if len(dq):
           print(dq[0])
       else:
           print(-1)

    elif command == 'back':
        if len(dq):
            print(dq[-1])
        else:
            print(-1)

    elif command == 'size':
        print(len(dq))

    elif command == 'empty':
        if len(dq):
            print(0)
        else:
            print(1)

    elif command == 'pop':
        if len(dq):
            print(dq[0])
            dq.popleft()
        else:
            print(-1)

for i in range(command_count):
    command_processor(input())