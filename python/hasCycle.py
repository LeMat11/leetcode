from ListNode import ListNode
def hasCycle(head:ListNode):
    Hash_map = set()
    curr = head
    while curr:
        if curr in Hash_map:
            return True
        Hash_map.add(curr)
        curr = curr.next
    return False