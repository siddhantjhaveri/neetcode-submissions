class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []  # This will be our Min-Heap
        
        # Add all initial numbers using the add method
        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:
        # Step 1: Add the new value to the heap
        heapq.heappush(self.heap, val)
        
        # Step 2: If we have more than k elements, remove the smallest
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        # Step 3: The root of the heap is the kth largest
        return self.heap[0]
        
