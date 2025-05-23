class Solution:
    def simplifyPath(self, path: str) -> str:
        
        result = []

        split_word = path.split("/")

        for word in split_word:
            if word == "" or word == ".":
                continue
            
            if word == ".." and result:
                result.pop()
                continue
            
            if word == "..":
                continue

            result.append(word)
            
        return "/" + "/".join(result)