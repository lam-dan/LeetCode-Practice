class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        print(roman_to_integer)

        # M C M X C I V

        # 1000 + 100 + 1000 + 10 + 100 + 1 + 5 = 2,216
         #  1000         900            90           4 = 1994

        # 5 => 4 => 104 => 94 => 1094 - 100 = 994 => 1000 = 1994
        total = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] in roman_to_integer:
                if s[i] == "I" and i < len(s) - 1 and (s[i + 1] == "V" or s[i + 1] == "X"):
                    total -= roman_to_integer[s[i]]
                elif s[i] == "X" and i < len(s) - 1 and (s[i + 1] == "L" or s[i + 1] == "C"):
                    total -= roman_to_integer[s[i]]
                elif s[i] == "C" and i < len(s) - 1 and (s[i + 1] == "D" or s[i + 1] == "M"):
                    total -= roman_to_integer[s[i]]
                else:
                    total += roman_to_integer[s[i]]
        return total

        # Time Complexity:
        # Theoretically O(n), where n is the length of the string.
        # But since valid Roman numerals only go up to 15 characters (for numbers ≤ 3999),
        # this function runs in constant time in practice: O(1).

        # Space Complexity:
        # O(1) — We use a fixed-size dictionary and a constant number of variables.




            