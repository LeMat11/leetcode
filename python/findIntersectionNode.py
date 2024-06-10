from ListNode import ListNode
def reverseList(head:ListNode):
    if not head:
        return head
    curr = None
    while head:
        temp = head.next
        head.next = curr
        curr = head
        head = temp
    return curr

def getIntersectionNode(headA:ListNode, headB:ListNode):
    headA = reverseList(headA)
    headB = reverseList(headB)
    if headA is not headB:
        return None
    while headA is headB:
        intersec = headA.val
        headA = headA.next
        headB = headB.next
    return intersec

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def main():
    headA = create_linked_list([1,9,1,2,4])
    headB = create_linked_list([3,2,4])
    res = getIntersectionNode(headA,headB)
    print(res)

main()