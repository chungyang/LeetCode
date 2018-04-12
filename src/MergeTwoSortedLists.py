# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class MergeTwoSortedLists:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        answer = current = ListNode(0)
        
        while l1 and l2:
            
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
                current = current.next
            elif l1.val > l2.val:
                current.next = l2
                l2 = l2.next
                current = current.next
            else:
                current.next = l1
                l1 = l1.next
                current = current.next
                current.next = l2
                l2 = l2.next
                current = current.next
          
        if l1 == None:
            current.next = l2
        elif l2 == None:
            current.next = l1
            
        return answer.next