class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = len(fruits)  # start with all fruits unplaced
        n = len(baskets)

        for fi in range(len(fruits)):  # loop over fruit indices
            for bi in range(n):        # loop over basket indices
                if baskets[bi] >= fruits[fi]:  # basket fits
                    baskets[bi] = -1           # mark as used
                    count -= 1                 # one less unplaced fruit
                    break                      # move to next fruit

        return count  # remaining unplaced fruits
            

            


