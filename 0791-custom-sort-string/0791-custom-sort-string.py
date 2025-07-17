class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # We need to reorder the string s so that the characters in order 
        # appear first (and in the given sequence), while any characters in 
        # s not present in order can appear anywhere after.
        
        # sorted_order = sorted(order)

        new_order = Counter(s)
        # new_order = set(s)
        print(new_order)
        result = []

        for i in range(len(order)):
            if order[i] in new_order:
                result.append(order[i] * new_order[order[i]]) # Append based on frequency count
                del new_order[order[i]] # delete from dictionary
    
        print(new_order)

        if len(new_order) > 0:
            for i in new_order:
                result.append(i * new_order[i])

        print(result)

        return "".join(result)
            

  


            

