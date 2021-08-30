"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
"""
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        
        for num in nums:
            self.add(num) # add elements using the function below
        
    def add(self, val: int) -> int:
        
        heapq.heappush(self.heap, val)
        
        # if after adding the new item causes 
        # the heap size to increase beyond k, 
        # then pop out the smallest element 
        if len(self.heap) > self.k: 
            heapq.heappop(self.heap)
            
        return self.heap[0] # the root element
"""
Runtime: 176 ms, faster than 25.29% of Python3 online submissions for Kth Largest Element in a Stream.
Memory Usage: 18.1 MB, less than 92.52% of Python3 online submissions for Kth Largest Element in a Stream.
"""
