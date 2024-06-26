def removeParenthese(s:str) -> str:
    left, right = 0,0
    result = []
    for char in s:
        if char == ')':
            right += 1
            if right > left:
                left, right = 0,0
                continue
            else: result.append(char)
        elif char == '(':
            left += 1
            result.append(char)
        else: result.append(char)
    result = ''.join(char for char in result)
    return result

s ="))lee(t(c)o)de)"
res = removeParenthese(s)
print(res) 
