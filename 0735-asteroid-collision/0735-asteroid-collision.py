class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in range(len(asteroids)):
            asteroid = asteroids[i]
            # positive vs negative asteroid
            # stack can't be empty
            while stack and stack[-1] > 0 and asteroid < 0:
                # 3 states
                # 1) two asteroids meet, smaller one explodes
                if stack[-1] < abs(asteroid):
                    stack.pop()
                    continue # Continue to next element
                elif stack[-1] > abs(asteroid):
                    break # Continue to next asteroid
                else:
                #2) If both are the same size, both will explode
                    stack.pop()
                    break
            #3) If both are moving in the same direction
            else:
                stack.append(asteroid)
        return stack