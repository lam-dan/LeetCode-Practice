class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # We need to reorder the string s so that the characters in order 
        # appear first (and in the given sequence), while any characters in 
        # s not present in order can appear anywhere after.

        new_order = Counter(s)
        result = []

        for i in range(len(order)):
            if order[i] in new_order:
                result.append(order[i] * new_order[order[i]]) # Append based on frequency count
                del new_order[order[i]] # delete from dictionary
    
        if len(new_order) > 0: # Any remaining elements in new_order
            for i in new_order: 
                result.append(i * new_order[i]) # Append at the end of result multiplied by the frequency

        return "".join(result)
            

  


            

