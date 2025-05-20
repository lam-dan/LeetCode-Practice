class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # Build an adjacency list where vertices current person and their neighbors or people that are richer
        adj_list = defaultdict(list)

        for rich, poor in richer:
            adj_list[poor].append(rich)

        print(adj_list)


        # Create a list of quiet people represented by the index
        # The value is the richer and more quieter person
        quietest = [None] * len(quiet)

        print(quietest)

        def dfs(i):
            # Base Case
            if quietest[i] is not None:
                return quietest[i]

            quietest_so_far = i

            for richer_person in adj_list[i]:
                # Want to see all of the richer people and compare if they are more quiet
                candidate = dfs(richer_person)
                # We take the candidate and quietest so far to look up their quiet factor from the quiet list to compare
                if quiet[candidate] < quiet[quietest_so_far]:
                    quietest_so_far = candidate
                
            quietest[i] = quietest_so_far

            return quietest_so_far
            # Iterate through neihbors

        for i in range(len(quiet)):
            dfs(i)

        return quietest
        


        # Create a quietest map based on the number of quiet of people
        # Output: [5,5,2,5,4,5,6,7]
        # answer[0] = 5
        # Why?

        # Richer chain: 0 ← 1 ← 3 ← 5

        # These people are as rich or richer than 0: [0, 1, 3, 5]
        # Their quiet values: [3, 2, 4, 1]

        # Quietest person is person 5 with quiet value 1
        # answer[7] = 7
        # Why?

        # Richer people than 7: 3 is richer than 7, and so are 4, 5, 6 (through 3)
        # But quiet values:

        # 7: 0

        # Others: [4,6,1,7] → min = 0 (still 7)
        # So even though 7 is at the bottom of the graph, they're the quietest among all possibly richer connections