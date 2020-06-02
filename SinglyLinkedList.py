class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at(prev_node, data):
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node


class LinkedList:

    def __init__(self):
        self.head = None

    def print(self):
        cur_list = self.head
        while cur_list:
            print(cur_list.data)
            cur_list = cur_list.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        next_node = self.head
        while next_node.next:
            next_node = next_node.next
        next_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        prev = None
        cur = self.head
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        prev.next = cur.next

    def delete_node_at_position(self, pos):
        prev = None
        cur = self.head
        c = 0
        while cur and c != pos:
            prev = cur
            cur = cur.next
            c += 1
        prev.next = cur.next

    def reverse_list(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            print(nxt.data)
            cur.next = prev
            print(cur.data)
            prev = cur
            print(prev.data)
            cur = nxt
            print(cur.data)
        self.head = prev

    def swap_nodes(self, node1, node2):
        prev1 = None
        current_node = self.head
        while current_node and current_node.data != node1:
            prev1 = current_node
            current_node = current_node.next

        prev2 = None
        current_node1 = self.head
        while current_node1 and current_node1.data != node2:
            prev2 = current_node1
            current_node1 = current_node1.next

        if prev1:
            prev1.next = current_node1

        else:
            self.head = current_node1

        if prev2:
            prev2.next = current_node
        else:
            self.head = current_node
        current_node.next, current_node1.next = current_node1.next, current_node.next


ls = LinkedList()
ls.append("A")
ls.append("B")
ls.append("C")
ls.append("D")
ls.swap_nodes('A', 'C')
ls.print()
