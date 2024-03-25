# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to start the merged list
        dummy = ListNode(0)
        # Pointer to traverse the merged list
        current = dummy

        # Traverse both lists until one of them becomes None
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach the remaining nodes of list1 or list2
        current.next = list1 if list1 else list2

        # Return the merged list, excluding the dummy node
        return dummy.next
     