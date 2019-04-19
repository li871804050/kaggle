# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    if l1.val >= l2.val:
        head = l2
        l2 = l2.next
    else:
        head = l1
        l1 = l1.next

    node = head
    while l1 != None and l2 != None:
        if l1.val >= l2.val:
            node.next = l2
            l2 = l2.next
        else:
            node.next = l1
            l1 = l1.next
        node = node.next
    if l1 == None:
        node.next = l2
    if l2 == None:
        node.next = l1
    return head

def add_list_node(list_nums:[])->ListNode:
    if len(list_nums) == 0:
        return None
    head = ListNode(list_nums[0])
    node = head
    for i in range(1, len(list_nums)):
        node_next = ListNode(list_nums[i])
        node.next = node_next
        node = node_next
    return head

def print_node(head):
    list = []
    while head != None:
        list.append(head.val)
        head = head.next
    print(list)

if __name__ == '__main__':
    n1 = [1,2,4]
    n2 = [1,3,4]
    l1 = add_list_node(n1)
    l2 = add_list_node(n2)
    print_node(l1)
    print_node(l2)
    node = mergeTwoLists(l1, l2)
    print_node(node)