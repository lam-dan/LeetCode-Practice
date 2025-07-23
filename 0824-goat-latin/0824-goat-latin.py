class Solution:
    def toGoatLatin(self, sentence: str) -> str:

        words = sentence.split(" ")

        vowels = {
            'a', 'e', 'i', 'o', 'u'
        }

        result = []
        
        for i in range(len(words)):
            # if the word begins with a vowel
            print(words[i][0])
            new_word = ""

            if words[i][0].lower() in vowels:
                new_word = words[i] + "ma"
            else:
                new_word = words[i][1:] + words[i][0] + "ma"
            
            new_word += (i + 1) * "a"
            result.append(new_word)
        print(result)
        return " ".join(result)

        





