class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            "I": 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        total = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] in mapping:
                if i < len(s) - 1:
                    if s[i] == "I" and (s[i + 1] == "V" or s[i + 1] == "X"):
                        total -= mapping[s[i]]
                    elif s[i] == "X" and (s[i + 1] == "L" or s[i + 1] == "C"):
                        total -= mapping[s[i]]
                    elif s[i] == "C" and (s[i + 1] == "D" or s[i + 1] == "M"):
                        total -= mapping[s[i]]
                    else:
                        total += mapping[s[i]]
                else:
                    total += mapping[s[i]]

        return total