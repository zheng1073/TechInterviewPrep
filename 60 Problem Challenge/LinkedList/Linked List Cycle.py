"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

def hasCycle(self, head: ListNode) -> bool:
        if head==None:
            return False
        slowPointer, fastPointer = head, head
        while(slowPointer and fastPointer):
            try:
                slowPointer, fastPointer = slowPointer.next, fastPointer.next.next
            except:
                return False
            if slowPointer == fastPointer:
                return True
        return False
        
