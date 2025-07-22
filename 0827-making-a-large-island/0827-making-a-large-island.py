class DisjointSet:
    def __init__(self, n):
        # Parent List:
        # Index: represents the child node id
        # Value: represents the parent node ID
        self.parent = list(range(n)) # Each node is initialized to be it's own parent
        self.size = [1] * n # Each node initially forms a component of size 1

    def find(self, x):
        # Find the represenative (root) of the component that x belongs to
        # If x is not it's own parent, recursively find it's parent root
        if self.parent[x] != x:
            # Path compression: flatten tree by making x point directly to the root
            self.parent[x] = self.find(self.parent[x])
        # return the root of x
        return self.parent[x]

    def union(self, x, y):
        # Find the roots of the two nodes
        rootX = self.find(x)
        rootY = self.find(y)

        # If they already share the same root, they are already connected
        if rootX == rootY:
            return

        # Union by size: attach smaller component under the larger one
        if self.size[rootX] < self.size[rootY]:
            # rootX is smaller, so it becomes a child of rootY
            self.parent[rootX] = rootY
            # Add the size of rootX to rootY's size
            self.size[rootY] += self.size[rootX]
        else:
            # rootY is smaller or equal, so it becomes a child of rootX
            self.parent[rootY] = rootX
            # Add the size of rootY to rootX's size
            self.size[rootX] += self.size[rootY]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # https://www.youtube.com/watch?v=lgiz0Oup6gM&ab_channel=takeUforward
        # Dynamically Changing the Graph by
        # Changing the cell value from 0 to 1 to connect
        # the cells in the graph
        # Intuition: Use Disjoint Set
        # Row, Col
        # 5 cols, 6 rows = 30 cells
        # (row x col) + col => nodeNo
        
        rows = len(grid)
        cols = len(grid[0])

        ds = DisjointSet(rows * cols)
        # down, up, right, left
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # Step 1: Union all adjacent land cells
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: #Only process if current cell is land
                    node_number = (r * cols) + c #Flatten (r, r) coordindates to a unique 1D node number

                    # Check all 4 neighboring directions
                    for dr, dc in directions:
                        new_r = r + dr # Compute neighbor's row index
                        new_c = c + dc # Compute neighbor's col index

                        if (
                            0 <= new_r < rows and
                            0 <= new_c < cols and
                            grid[new_r][new_c] == 1
                        ):
                            # Flatten neighbor's coordinates to 1D index
                            neighbor_number = new_r * cols + new_c
                            # Union the current land cell with the neighboring land cell
                            ds.union(node_number, neighbor_number)

        # === PURPOSE: Track the largest island formed after any flip ===
        # Initialize the maximum island size found
        max_island_size = 0
        # === PURPOSE: Detect if there is any zero cell at all ===
        # Flag to indicate whether any zero was encountered in the grid
        has_zero = False
        # === PURPOSE: Used during flip evaluation to avoid double-counting islands ===
        unique_roots = set() # Stores unique neighboring island roots around the flipped cell from 0 to 1
        
        # Step 2: Try flipping each zero to one and calculate potential island size
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: # Only process water cells 0
                    has_zero = True # Mark that grid contains at least one zero
                    current_island_size = 1

                    # Check all 4 neighboring directions
                    for dr, dc in directions:
                        new_r = r + dr # Calculate neighbor's rows
                        new_c = c + dc # Calculate neighbor's col

                        # If the neighbor is within bounds and is land
                        if (
                            0 <= new_r < rows and
                            0 <= new_c < cols and
                            grid[new_r][new_c] == 1
                        ):
                            neighbor_number = (new_r * cols) + new_c # Flatten the neighbor to 1D index
                            # Find the root of the neighbor's island
                            root = ds.find(neighbor_number)
                            #Add the root to the set to avoid duplicates
                            unique_roots.add(root)

                    # Sum the sizes of all unique neighboring islands
                    for root in unique_roots:
                        current_island_size += ds.size[root]

                    # Clear the set for the next zero
                    unique_roots.clear()
                    # Update the max island size if the current size is larger
                    max_island_size = max(max_island_size, current_island_size)
        # If no zero was found, the grid is already all land
        if not has_zero:
            # The entire grid is one big island
            return rows * cols
        # Return the largest island size possible after flipping one zero
        return max_island_size
            
                




                    







        
