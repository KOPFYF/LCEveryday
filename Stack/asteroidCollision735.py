# ast > 0 fly to right, won't crash previous
# ast < 0 fly to left, if previous same dir, won't crash either
# ast < 0 fly to left, previous fly to right, crash(previous crash, ast crash, both crash)

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            # print(stack)
            if ast > 0: # fly to right, no crash
                stack.append(ast)
            elif not stack or stack[-1] < 0: # no prev or prev to the left
                stack.append(ast)
            else:
                while stack and stack[-1] > 0 and stack[-1] < -ast:
                    # right < left, keep crashing(while)
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(ast)
                elif stack[-1] == -ast:
                    stack.pop()
            
        return stack