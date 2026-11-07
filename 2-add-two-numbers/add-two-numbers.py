from itertools import zip_longest

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        def values(head):
            while head is not None:
                yield head.val
                head = head.next

        dummy = ListNode(0)
        current = dummy
        carry = 0

        for a, b in zip_longest(values(l1), values(l2), fillvalue=0):
            carry, digit = divmod(a + b + carry, 10)
            current.next = ListNode(digit)
            current = current.next

        if carry:
            current.next = ListNode(carry)

        return dummy.next
