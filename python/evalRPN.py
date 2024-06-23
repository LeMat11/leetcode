from typing import List

def evalRPN(tokens: List[str]) -> int:
    stack = []
    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.append(int(token))
        else:
            pop1 = stack.pop()
            pop2 = stack.pop()
            if token == '+':
                stack.append(pop2 + pop1)
            elif token == '-':
                stack.append(pop2 - pop1)
            elif token == '*':
                stack.append(pop2 * pop1)
            elif token == '/':
                # In Python, integer division behaves like Math.trunc in JavaScript
                stack.append(int(pop2 / pop1))
            else:
                raise ValueError("Invalid operator")
    return stack[0]

def main():
    token = ["2","1","+","3","*"]
    res = evalRPN(token)
    print(res)

main()
