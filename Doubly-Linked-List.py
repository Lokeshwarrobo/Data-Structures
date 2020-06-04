class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Doubly_Linked_List:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        cur_node = self.head
        if self.head is None:
            self.head = new_node
            self.head.prev = None
        else:
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.prev = cur_node
            new_node.next = None

    def prepend(self, data):
        if self.head is None:
            self.head = Node(data)
            self.head.prev = None
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = None
            self.head = new_node

    def add_after_node(self, key, data):
        cur_node = self.head
        while cur_node and cur_node.data != key:
            cur_node = cur_node.next
        new_node = Node(data)
        nxt = cur_node.next
        cur_node.next = new_node
        new_node.next = nxt
        new_node.prev = cur_node
        nxt.prev = new_node

    def add_before_node(self, key, data):
        cur_node = self.head
        while cur_node and cur_node.data != key:
            cur_node = cur_node.next
        prevs = cur_node.prev
        new_node = Node(data)
        prevs.next = new_node
        cur_node.prev = new_node
        new_node.next = cur_node
        new_node.prev  = prevs

    def delete_node(self, key):
        cur_node = self.head
        while cur_node and cur_node.data != key:
            cur_node = cur_node.next
        pre = cur_node.prev
        pre.next = cur_node.next
        cur_node.prev = None



    def print_list(self):
        cur_list = self.head

        while cur_list:
            print(cur_list.data)
            cur_list = cur_list.next

dl = Doubly_Linked_List()
dl.append(1)
dl.append(2)
dl.append(3)
dl.append(4)
dl.append(5)
dl.delete_node(2)
dl.add_before_node(3, 2)
dl.add_after_node(1, 2)
dl.print_list()
