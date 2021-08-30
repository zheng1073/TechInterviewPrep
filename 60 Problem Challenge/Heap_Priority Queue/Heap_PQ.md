## Heap/Binary Heap
- import heapq as hq
- heap = []
- hq.heappop(heap)
- hq.heappush(heap,val)
> Heap as a tree: left child of node (index i) has index (2i)+1 and right child has index (21)+2

## Priority Queue
>**Abstract Data Type** : set of behaviors defined for a data type. It's abstract because it's implementation is flexible so long it has the behaviors.
- Implemented in Python as a list of tuples 
  - listOfStrings = [(_priority_, _value_), (2, "String 1"), (4, "String 5")]  
  - hq.heapify(listOfStrings)
