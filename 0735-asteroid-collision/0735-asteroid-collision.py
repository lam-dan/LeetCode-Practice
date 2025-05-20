class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Relative position in space based on index
        # absolute value = size
        # sign represents direction (+, right), (-, left)
        # two asteroids meet, smaller will explodes
        # if the same size, both explode
        # else asteroids never meet

        # (5, right) size 5
        # (10, right) size 10

        # (-5, left) size 5 (deleted)

        # Stack for processing
        # compare each value before putting it into the stack
        stack = []

        for current in asteroids:
            # Incoming left-moving asteroid
            # A lot of conditions for the stack
            # Stack has to have something
            # asteroids in stack have to be positive
            # current incoming asteroid must be negative
            while stack and stack[-1] > 0 and current < 0:
                if stack[-1] < abs(current):
                    stack.pop() # top asteroid in stack explodes
                    continue # keep checking current asteroid against next top asteroid
                # if the size of asteroids are the same between top and incoming
                elif stack[-1] == abs(current):
                    stack.pop() # top asteroid in stack explodes
                break # current asteroid also explodes
            else:
                # Either stack is empty or no collision -> safe to add
                stack.append(current)
        return stack

                
                

            



