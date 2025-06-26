import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Step 1: Build a max-heap of size k using the first k points
        # We negate the squared distance to simulate a max-heap with Python's min-heap behavior
        heap = [(-x**2 - y**2, x, y) for x, y in points[:k]]
        heapq.heapify(heap)  # Heapify in O(k) time

        # Step 2: Iterate over the remaining points
        for x, y in points[k:]:
            
            # Compute negated squared distance (to avoid sqrt, squared distance suffices for comparison)
            dist = -x**2 - y**2

            
            # If this point is closer than the farthest point currently in heap
            if dist > heap[0][0]:
                # Replace the farthest point with this one using heappushpop
                # Keeps heap size constant at k
                # heapq.heappushpop(heap, (dist, x, y))
                heapq.heappush(heap, (dist, x, y))
                heapq.heappop(heap)

        # Step 3: Extract the k closest points from the heap
        # Since heap stores (neg_distance, x, y), extract x and y only
        return [[x, y] for (_, x, y) in heap]