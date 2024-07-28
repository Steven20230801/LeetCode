class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def print_list(lst):
    linked_list = linked_list(lst)
    current = linked_list
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next


def print_head(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next
