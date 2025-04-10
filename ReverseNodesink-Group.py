class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    class Stack:

        class Node:
            def __init__(self, value: object):
                self.value = value
                self.tail = None

        def __init__(self):
            self.head = None

        def push(self, value: object):
            node = self.Node(value)
            if self.head is None:
                self.head = node
            else:
                node.tail = self.head
                self.head = node

        def pop(self) -> Node:
            if self.head is None:
                raise ValueError('Stack is empty')
            else:
                k = self.head
                self.head = k.tail
                k.tail = None
                return k

    def create_list(self, k: int) -> ListNode:
        num = 1
        node = ListNode(num)
        c = node
        while num < k:
            c.next = ListNode(num + 1)
            num += 1
            c = c.next
        return node

    def print_list(self, node: ListNode) -> str:
        result = '[ '
        c = node
        while c:
            result += str(c.val) + ' '
            c = c.next
        result += ']'
        return result

    def gen_len(self, node: ListNode) -> int:
        length = 0
        c = node
        while c:
            c = c.next
            length += 1
        return length

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        start = ListNode()
        stack = self.Stack()
        c = head
        g = start
        i = 0
        for l in range(self.gen_len(head) // k):
            while i < k:
                stack.push(c)
                c = c.next
                i += 1

            node = stack.pop().value
            j = node
            i -= 1
            while i > 0:
                j.next = stack.pop().value
                i -= 1
                j = j.next
            j.next = None
            g.next = node
            while g.next:
                g = g.next
        g.next = c
        return start.next
