
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def add(list):
    head = ListNode(list[0])
    next = None
    for i in range(1, len(list)):
        node = ListNode(list[i])
        if next == None:
            head.next = node
            next = node
        else:
            next.next = node
            next = node
    return head

def to_str(head):
    s = ''
    while head != None:
        s += ' ' + str(head.val)
        head = head.next
    return s


def mergeKLists(lists) -> ListNode:
    if len(lists) == 0:
        return []
    while True:
        lists_n = []
        l = len(lists) - 1
        for i in range(l):
            if i > l - i:
                break
            elif i == l - i:
                lists_n.append(lists[i])
                break
            lists_n.append(merge([lists[i], lists[l - i]]))
        if len(lists_n) > 0:
            lists = lists_n
        if len(lists) <= 1:
            break
    if lists == None or len(lists) < 1:
        return []
    return lists[0]


def merge(lists: [ListNode]) -> ListNode:
    if len(lists) == 0:
        return []
    for i in range(1, len(lists)):
        head = lists[0]
        insert = lists[i]
        while True:
            if head == None:
                head = insert
                lists[0] = head
                break
            if insert == None:
                break
            if insert.val >= head.val:
                if head.next == None:
                    head.next = insert
                    break
                elif head.next.val > insert.val:
                    insertNext = insert.next
                    headNext = head.next
                    head.next = insert
                    insert.next = headNext
                    insert = insertNext
                    head = head.next
                else:
                    head = head.next
            else:
                insertNext = insert.next
                insert.next = head
                head = insert
                insert = insertNext
                lists[0] = head
    return lists[0]

def reverseKGroup(head, k):
    if head == None:
        return head
    cou = 1
    nhead = head
    n_head = None
    n_end = None
    while nhead != None:
        if cou == k:
            next_n = nhead.next
            nhead.next = None
            start, end = turn_down(head)

            if n_head == None:
                n_head = start
                n_end = end
            else:
                n_end.next = start
                n_end = end
            head = next_n
            if head == None:
                break
            nhead = head
            cou = 1
        else:
            nhead = nhead.next
            cou += 1
    if n_end != None:
        n_end.next = head
        return n_head
    return head




def turn_down(head):
    if head == None:
        return head
    end = head
    next_node = head.next
    start = 0
    while next_node != None:
        if start == 0:
            head.next = None
            start = 1
        next_n = next_node.next
        next_node.next = head
        head = next_node
        next_node = next_n
    return head,end

def swapPairs(head: ListNode):
    if head == None:
        return head
    next_n = head.next
    head_n = head
    head_p = head
    start = 0
    while next_n != None and head_n != None:
        next_nn = next_n.next
        next_n.next = head_n
        head_n.next = next_nn
        if start == 0:
            start = 1
            head = next_n
        else:
            head_p.next = next_n
            head_p = head_n
        head_n = next_nn
        if head_n != None:
            next_n = head_n.next
    return head

if __name__ == '__main__':
    # lists.append(add(c))
    node = add([1, 2, 3, 4])
    print(to_str(swapPairs(node)))