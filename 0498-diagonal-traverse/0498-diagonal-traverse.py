class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        result = []
        # Shared Indicies of All Diagonal are equal
        # [1,2,3]
        # [4,5,6]
        # [7,8,9]
        # 2, 4 are on the same diagonal, and they share the index sum of 1. 
        # - 2 is matrix[0][1] and 4 is in matrix[1][0]. 
        # 3,5,7 are on the same diagonal, and they share the sum of 2. 
        # - 3 is matrix[0][2], 5 is matrix[1][1], and 7 is matrix [2][0].

        # SO, if you can loop through the matrix, store each element by the 
        # sum of its indices in a dictionary, you have a collection of all 
        # elements on shared diagonals.
        # {0: [1], 1: [2, 4], 2: [3, 5, 7], 3: [6, 8], 4: [9]}

        # The last part is easy, build your answer (a list) by elements on diagonals. 
        # To capture the 'zig zag' or 'snake' phenomena of this problem, simply 
        # reverse ever other diagonal level. So check if the level is divisible by 2.
        diagonals = {}
        for i in range(rows):
            for j in range(cols):
                if i + j not in diagonals:
                    diagonals[i + j] = [mat[i][j]]
                else:
                    diagonals[i + j].append(mat[i][j])

        print(diagonals)
        result = []
        # {0: [1], 1: [2, 4], 2: [3, 5, 7], 3: [6, 8], 4: [9]}
        # result = [1,2,4,7,5,3,6,8,9]
        # As you can see above, r + c indexes 0, 2, 4 are apppended
        # into the array in reverse order [3,5,7] in dictionary
        # result 
        for i in range(len(diagonals)):
            if i % 2 == 0: # if index of the row is even we append backwards
                for j in range(len(diagonals[i]) - 1, -1, -1):
                    result.append(diagonals[i][j])
            else: # if index of the row is odd, we append forwards
                for j in range(len(diagonals[i])): 
                    result.append(diagonals[i][j])
        return result

            

            
        
        

        
