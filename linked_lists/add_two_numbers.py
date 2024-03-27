from typing import *


class ListNode:
    def __init__(self, value=0, nxt=None):
        self.value = value
        self.nxt = nxt

    def insert_next_value(self, value, nxt=None):
        l1 = ListNode(value)

        if self is None:
            return l1
        current = self
        while current.nxt is not None:
            current = current.nxt
        current.nxt = l1
        return self




class AddTwoNumbers:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        carry = 0

        ### This was my approach
        while (l1 is not None) and (l2 is not None):
            total = str(l1.val + l2.val + carry)
            if len(total) > 1:
                curr = total[1]
                carry = int(total[0])
            else:
                curr = total[0]
                carry = 0
            res.append(curr)
            l1 = l1.next
            l2 = l2.next

        if l1 is None:
            while l2 is not None:
                total = str(l2.val + carry)
                if len(total) > 1:
                    curr = total[1]
                    carry = int(total[0])
                else:
                    curr = total[0]
                    carry = 0
                res.append(curr)
                l2 = l2.next

        if l2 is None:
            while l1 is not None:
                total = str(l1.val + carry)
                if len(total) > 1:
                    curr = total[1]
                    carry = int(total[0])
                else:
                    curr = total[0]
                    carry = 0
                res.append(curr)
                l1 = l1.next
        if carry != 0:
            res.append(carry)

        ### Simpler way to reduce the loops
        #### while l1 is not None or l2 is not None or carry!=0:
        ####        digit = sum%10
        ####        carry = sum//10

        output = ListNode(res[-1])
        for i in res[-2::-1]:
            temp = ListNode(i, output)
            output = temp
        return output


if __name__ == "__main__":
    print('main started')
    l1 = ListNode(3)
    print(vars(l1))
    l2 = ListNode(4, l1)
    print(vars(l2))
    l1.insert_next_value(7)
    print(vars(l1))
    print(vars(l1.nxt))