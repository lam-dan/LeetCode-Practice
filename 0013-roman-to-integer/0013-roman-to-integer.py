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
        for i in range(len(s)- 1, -1, -1):
            print("s[i]", s[i])
            if s[i] in roman_to_integer:
                if s[i] == "I":
                    if 0 <= i < len(s) - 1 and (s[i + 1] == "V" or s[i + 1] == "X"):
                        total -= roman_to_integer[s[i]]
                    else:
                        total += roman_to_integer[s[i]]
                elif s[i] == "X":
                    if 0 <= i < len(s) - 1 and (s[i + 1] == "L" or s[i + 1] == "C"):
                        total -= roman_to_integer[s[i]]
                    else:
                        total += roman_to_integer[s[i]]
                elif s[i] == "C":
                    if 0 <= i < len(s) - 1 and (s[i + 1] == "D" or s[i + 1] == "M"):
                        total -= roman_to_integer[s[i]]
                    else:
                        total += roman_to_integer[s[i]]
                else:
                    total += roman_to_integer[s[i]]
                    print("total", total)
        return total


            