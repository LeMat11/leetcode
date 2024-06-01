class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sortList(head:ListNode) -> ListNode:
    if not head:
        return head
    
    node = head
    res = []

    while node:
        res.append(node.val)
        node = node.next
    res.sort(reverse=True)
    node = head

    while node:
        node.val = res.pop()
        node = node.next

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
    arr = [4, 2, 1, 3]
    head = create_linked_list(arr)
    solution = sortList(head)
    print_linked_list(solution)