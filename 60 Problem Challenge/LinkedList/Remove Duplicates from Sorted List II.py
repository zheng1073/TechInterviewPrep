"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
"""
def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        try:
            nextNode = head.next
            while (head.val == nextNode.val):
                try:
                    head = nextNode.next
                    if head.val == nextNode.val:
                        head = nextNode
                        nextNode = head.next
                except:
                    head = None
                    return head
            prev = head
            #current, nextNode = head, head.next
            current = prev
            nextNode = current.next
            while (nextNode != None):
                while (current.val == nextNode.val):
                    try:
                        if prev == current or nextNode == prev:
                            try:
                                head = nextNode.next
                                prev = head
                            except:
                                head = None
                        current = nextNode.next
                        if current.val == nextNode.val:
                            current = nextNode
                            nextNode = current.next
                        else:
                            if prev != current:
                                prev.next = current
                    except:
                        prev.next = None
                        return head
                nextNode = current.next
                if (current.val != nextNode.val):
                    prev = current
                    current = prev.next
                    nextNode = current.next
                    
            return head
        except:
            return head
"""
Runtime: 36 ms, faster than 90.32% of Python3 online submissions for Remove Duplicates from Sorted List II.
Memory Usage: 14.3 MB, less than 58.86% of Python3 online submissions for Remove Duplicates from Sorted List II.
"""
