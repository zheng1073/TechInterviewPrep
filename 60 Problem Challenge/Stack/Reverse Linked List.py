"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while (current != None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev
"""
Runtime: 52 ms, faster than 9.62% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.5 MB, less than 93.29% of Python3 online submissions for Reverse Linked List.
"""
"""
tried to use stack but didn't work oop: TRY AGAIN
"""
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None):
            return None
        if (head.next == None):
            return head
        # create Stack and put head in there
        stack = []
        current, nextNode = head, head.next
        while (nextNode != None):
            stack.append(head)
            head.next = current
            current.next = nextNode
            head = current
            current, nextNode = head, head.next
        current = stack.pop()
        head.next = current
        while (len(stack) > 0):
            nextNode = stack.pop()
            current.next = nextNode
            current = nextNode
        return head
"""
a
"""
