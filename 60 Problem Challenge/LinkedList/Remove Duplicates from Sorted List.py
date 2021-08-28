"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
"""
def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        try:
            current, nextNode = head, head.next
            while (nextNode != None):
                while (current.val == nextNode.val):
                    try:
                        nextNode = nextNode.next
                        current.next = nextNode
                    except:
                        current.next = None
                current = nextNode
                nextNode = nextNode.next
            return head
                
        except:
            return head
"""
Runtime: 40 ms, faster than 80.45% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 14.3 MB, less than 55.79% of Python3 online submissions for Remove Duplicates from Sorted List.
"""
