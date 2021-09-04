'''
Sort a list of all orders in the order queue to assist in prioritization of fullfilment. They should be sorted in the following order:

1. Prime orders should be returned first (metadata only lowercase letters/sorted lexicographically) then non-Prime.  
2. In case there is a tie, the identifier should be used.
3. The remaining non-Prime order will remain in the order that they came in.

Input: orderList (list of strings representing all orders) 
Output: list of orders
'''
# Overall time complexitiy: O(NlogN)
def taskPrioritization(orderList):
  # split task into 3 categories (Prime orders and non-prime order) 
  # Time Complexitity: O(N)
  prime, regular = [], []
  for order in orderList:
    x, y = order.split(" ", 1)
    y = y.replace(" ", "")
    if y.isdigit():
      regular.append(order)
     else:
      prime.append(order)
  
  # Sort Prime order
  # Time Complexitiy: O(NlogN)
  prime.sort(key = lambda x : (x.split(" ")[1]))
  i, j = 0, 1
  while i < (len(prime)-1) and j < len(prime):
    x0, y0 = prime[i].split(" ", 1)
    x1, y1 = prime[j].split(" ", 1)
    y0, y1 = y0.replace(" ", ""), y1.replace(" ", "")
    if y0 == y1:
      prime = sortHelper(i, j, prime)
      j = j + 1
    else:
      i = j
      j = i + 1
      
  # Merge the two list
  # Time Complexitiy: O(1)
  finalOrder = prime + regular
  
  # Return final list
  return finalOrder

# helper function
def sortHelper(i, j, prime):
  partOne = prime[:i]
	partTwo = prime [i:j+1]
	partThree = prime[j+1:]
	
	partTwo.sort(key = lambda x : (x.split(" ")[0]))

	prime = partOne + partTwo + partThree
	return prime
