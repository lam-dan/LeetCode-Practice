class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(" ")
        vowels = {
            'a', 'e', 'i', 'o', 'u'
        }
        result = []
        
        for i in range(len(words)):
            new_word = ""
            if words[i][0].lower() in vowels:
                new_word += words[i] + "ma"
            else:
                new_word += words[i][1:] + words[i][0] + "ma"
            new_word += "a" * (i + 1)
            result.append(new_word)
        return " ".join(result)

        # Time Complexity is O(n^2)
        # Space Complexity is O(n^2)



