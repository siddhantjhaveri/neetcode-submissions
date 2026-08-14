class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Step 1: Create a Max-Heap using negative values
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)  # Turns the list into a heap in O(n) time
        
        # Step 2: Keep smashing until 1 or 0 stones remain
        while len(max_heap) > 1:
            # Pop the two heaviest stones
            y = -heapq.heappop(max_heap)  # Heaviest (remember, pop gives negative)
            x = -heapq.heappop(max_heap)  # Second heaviest
            
            # If they are not equal, the heavier one survives with reduced weight
            if x != y:
                # Only push back if they are different
                heapq.heappush(max_heap, -(y - x))
        
        # Step 3: Return the last stone, or 0 if none remain
        return -max_heap[0] if max_heap else 0
        