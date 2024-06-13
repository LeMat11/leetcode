from ListNode import ListNode
def reverseBetween(head:ListNode,left,right):
    if not head:
        return head
    count = int(1)
    curr = head
    pre = None
    front, back, temp = ListNode(),ListNode(),ListNode()
    while count < left:
        temp = curr
        curr = curr.next
        count += 1
    front, back = temp, curr
    while count <= right:
        temp = curr.next
        curr.next = pre
        pre = curr
        curr = temp
        count += 1
    if pre:
        front.next = pre
    else:
        front.next = curr
    if back: 
        back.next = curr
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
    # arr = [1,2,3,7,4,5,6]
    arr = [5,3]
    head = create_linked_list(arr)
    solution = reverseBetween(head,1,2)
    print_linked_list(solution)
    