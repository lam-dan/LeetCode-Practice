class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        target_triplet = set()
        
        for i in range(len(triplets)):
            if ( 
                triplets[i][0] > target[0] or 
                triplets[i][1] > target[1] or 
                triplets[i][2] > target[2]):
                continue
            
            if triplets[i][0] == target[0]:
                target_triplet.add(0)
            if triplets[i][1] == target[1]:
                target_triplet.add(1)
            if triplets[i][2] == target[2]:
                target_triplet.add(2)

        return len(target_triplet) == len(target)

        # Time Complexity is O(n)
        # Space Complexity is O(1) - we store at max 3 triplets so it's constant space