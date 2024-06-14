from ListNode import ListNode
def oddEvenList(head:ListNode):
    if not head or not head.next:
        return head
    curr = head
    even = head.next
    even_cr = even
    while curr.next and curr.next.next:
        curr.next = curr.next.next
        curr = curr.next
        even_cr.next = even_cr.next.next
        even_cr = even_cr.next
    if even:
        curr.next = even
    return head

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    vals = []
    current = head
    while current:
        vals.append(current.val)
        current = current.next
    print(vals)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    # arr = [5,3]
    head = create_linked_list(arr)
    solution = oddEvenList(head)
    print_linked_list(solution)