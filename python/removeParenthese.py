def removeParenthese(s:str) -> str:
    stack = []
    s = list(s)
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                s[i] = ''
    
    while stack:
        s[stack.pop()] = ''

    result = ''.join(s)
    return result

s ="))lee(t(c)o)de)"
s = '))((' 
res = removeParenthese(s)
print(res) 
