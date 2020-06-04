class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Circular_Linked_List:

    def __init__(self):
        self.head = None

    def append(self, data):

        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head                  
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head


    def prepend(self, data):
        new_node = Node(data)
        cur_node = self.head
        new_node.next = self.head
        if self.head is None:
            self.head = new_node
        else:
            while cur_node.next != self.head:
                cur_node = cur_node.next
            cur_node.next = new_node
        self.head = new_node

    def __len__(self):
        cur_node = self.head
        l = 0
        while cur_node :
            l += 1
            cur_node = cur_node.next
            if cur_node == self.head:
                break
        return l

    def split(self):
        size = len(self)
        mid = size // 2
        count = 0
        cur = self.head
        prev = None
        while cur and count < mid:
            prev = cur
            cur = cur.next
            count += 1
        prev.next = self.head

        split2 = Circular_Linked_List()
        while cur.next != self.head:
            split2.append(cur.data)
            cur = cur.next
        split2.append(cur.data)
        CL.print_list()
        print("\n")
        split2.print_list()

    def remove_element(self, key):
        if self.head.data == key:
            prev = None
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            prev = None
            cur = self.head
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                while cur.data == key:
                    prev.next = cur.next
                    cur = cur.next
    def remove_node(self, node):
        if self.head == node:
            prev = None
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            prev = None
            cur = self.head
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                while cur == node:
                    prev.next = cur.next
                    cur = cur.next

    def josephus_circle(self, step):
        cur = self.head
        while len(self)>1:
            count = 1
            while count != step:
                cur = cur.next
                count += 1
            self.remove_node(cur)
            cur = cur.next
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break



CL = Circular_Linked_List()
CL.append("A")
CL.append("B")
CL.append("C")
CL.append("D")
CL.prepend("E")
CL.josephus_circle(3)
CL.print_list()