# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # curr_1 = list1
        # curr_2 = list2        
        # if curr_2 is None:
        #     return curr_1
        # head = curr_1 if curr_1 is not None and curr_1.val < curr_2.val else curr_2
        # while curr_1:
        #     if curr_1.val <= curr_2.val and (curr_2.next or curr_1.val < curr_2.next.val if curr_2.next else False):
        #         curr_1.next = curr_2
        #         curr_2 = curr_1
        #         head = curr_2
        #     elif curr_2.next is not None and curr_2.val <= curr_1.val < curr_2.next.val :
        #         nxt = curr_2.next
        #         curr_2.next = curr_1
        #         curr_1.next = nxt
        #     elif curr_1.val > curr_2.val and curr_2.next is None:
        #         curr_2.next = curr_1
        #         break
        #     else:                
        #         curr_1 = curr_1.next             

        # return head

        # curr_1 = list1
        # curr_2 = list2 
        # if curr_1 is None:
        #     head=curr_2
        #     return head
        # elif curr_2 is None:
        #     head=curr_1
        #     return head
        # elif curr_1.val < curr_2.val:
        #     head=curr_1
        # else:
        #     head=curr_2

        # while curr_1:
        #     if curr_2.next is None:
        #         if curr_1.val > curr_2.val: 
        #             curr_2.next = curr_1
        #             curr_1 = curr_1.next
        #         else:
        #             nxt = curr_1.next
        #             curr_1.next = curr_2
        #             curr_1 = nxt
        #     elif curr_2.val <= curr_1.val < curr_2.next.val:
        #         nxt_curr = curr_1.next
        #         nxt = curr_2.next
        #         curr_2.next = curr_1
        #         curr_1.next = nxt
        #         curr_1 = nxt_curr
        #     elif curr_1.val < curr_2.val:
        #         nxt = curr_1.next
        #         curr_1.next = curr_2
        #         curr_1 = nxt
        #     else:
        #         print("Oops  i thought this shouldn't happen")
        #         print(curr_1)
        #         print(curr_2)
        
        # return head

        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        tail.next = list1 or list2
        return dummy.next


