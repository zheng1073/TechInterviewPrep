'''
Sort a list of all orders in the order queue to assist in prioritization of fullfilment. They should be sorted in the following order:

1. Prime orders should be returned first (metadata only lowercase letters/sorted lexicographically) then non-Prime.  
2. In case there is a tie, the identifier should be used.
3. The remaining non-Prime order will remain in the order that they came in.

Input: orderList (list of strings representing all orders) 
Output: list of orders
'''

def taskPrioritization(orderList):
  
