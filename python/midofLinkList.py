class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def middleNode(head:ListNode):
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next
        fast = fast.next
        slow = slow.next
    return slow

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
    head = create_linked_list(arr)
    solution = middleNode(head)
    print_linked_list(solution)
        