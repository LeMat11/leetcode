from typing import List

def asteroidCollision(asteroids: List[int]) -> List[int]:
    stack = []

    for asteroid in asteroids:
        if not stack: 
            stack.append(asteroid)
        else:
            while asteroid<0 and stack[-1] * asteroid<0:
                if abs(stack[-1])<abs(asteroid):
                    stack.pop()
                    if stack: continue
                    else: 
                        stack.append(asteroid)
                        break
                elif abs(stack[-1])> abs(asteroid):
                    break
                elif stack[-1] == -asteroid:
                    stack.pop()
                    break
            else: stack.append(asteroid)

    return stack

asteroids = [1,-2,-2,-2]
res = asteroidCollision(asteroids)
print(res)