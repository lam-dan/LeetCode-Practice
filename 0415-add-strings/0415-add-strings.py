class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Intuition - doing math by hand, we start from the right hand side of the numbers
        # so we need 2 points for each string
        ptr1 = len(num1) - 1
        ptr2 = len(num2) - 1
        carry = 0
        result = []

        while ptr1 >= 0 or ptr2 >= 0 or carry:
            # Figure out the value of each string

            digit1 = ord(num1[ptr1]) - ord('0') if ptr1 >= 0 else 0
            digit2 = ord(num2[ptr2]) - ord('0') if ptr2 >= 0 else 0

            total = digit1 + digit2 + carry
            result.append(str(total % 10))

            carry = total // 10 

            ptr1 -= 1
            ptr2 -= 1

        return "".join(result[::-1])





