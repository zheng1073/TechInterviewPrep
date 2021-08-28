"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.
"""
def detectCycle(self, head: ListNode) -> ListNode:
        dict_tracker = {}
        currentNode, index = head, 0
        while (currentNode != None):
            if (currentNode not in dict_tracker):
                dict_tracker[currentNode] = index
                currentNode, index = currentNode.next, index + 1
            else:
                return currentNode
        return None
      
      """
      Runtime: 44 ms, faster than 93.85% of Python3 online submissions for Linked List Cycle II.
      Memory Usage: 17.4 MB, less than 22.71% of Python3 online submissions for Linked List Cycle II.
      """
