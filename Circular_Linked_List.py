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
CL.print_list()