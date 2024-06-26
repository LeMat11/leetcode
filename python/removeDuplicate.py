def removeDuplicate(s: str, k: int) -> str:
    stack = []
    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
            if stack [-1][1] == k:
                stack.pop()
        else:
            stack.append([char,1])
    result = ''.join(char * count for char, count in stack)
    return result

s = "deeedbbcccdbaa"
k = 3
print(removeDuplicate(s, k))