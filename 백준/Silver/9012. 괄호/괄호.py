T = int(input())

for i in range(0, T):

    t = input()
    stack = []
    for j in range(0, len(t)):
        stack.append(t[j])
        if stack[0] + stack[-1] == '()':
            stack.pop(-1)
            stack.pop(0)

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')