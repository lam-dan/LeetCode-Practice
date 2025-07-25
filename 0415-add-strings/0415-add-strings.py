class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1 # right pointer for num1 at end of the string
        j = len(num2) - 1 # right pointer for num2 at end of the string
        carry = 0 # initial value of carry
        result = []

        # Loop until both pointers are exhausted and no carry remains
        while i >= 0 or j >= 0 or carry:
            # Get the digit from num1 at position if i is valid, else 0
            digit1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            digit2 = ord(num2[j]) - ord('0') if j >= 0 else 0

            # Compute the total of both digits and the carry from the previous step
            total = digit1 + digit2 + carry

            # Append the least significant digit of the total to the result
            result.append(str(total % 10))

            # Update the carry to be used in the next iteration (1 if total >= 10, else 0)
            carry = total // 10

            # Move to the next significant digit (left)
            i -= 1
            j -= 1
        # At this point, result holds digits in reverse order, so we reverse it and join into a string
        return ''.join(reversed(result))


