import sys

stack = []

for i in range(int(sys.stdin.readline())): # 처음에 명령어의 갯수를 알려줌
    command = sys.stdin.readline().split() # 읽으면서 공백문자로 구분
    if command[0] == 'push':
        stack.append(int(command[1])) # 문자열이므로 int 타입으로 수정
    elif command[0] == 'pop':
        if len(stack) == 0: print(-1)
        else: print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0: print(1)
        else: print(0)
    else: #  'top'
        if len(stack) == 0: print(-1)
        else: print(stack[-1])