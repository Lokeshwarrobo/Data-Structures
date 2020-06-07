class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Queue(object):

    def __init__(self):
        self.list = []

    def enqueue(self, data):
        self.list.insert(0, data)

    def dequeue(self):
        if not self.is_empty():
            return self.list.pop()

    def is_empty(self):
        return len(self.list) == 0

    def peek(self):
        if not self.is_empty():
            return self.list[-1].data

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.list)

class Binary_Tree(object):

    def __init__(self, root):
        self.root = Node(root)

    def print_transersal(self, transversal_type):
        if transversal_type == 'preorder':
            return self.pre_order(BT.root, '')
        elif transversal_type == 'inorder':
            return self.in_order(BT.root, "")
        elif transversal_type == 'postorder':
            return self.in_order(BT.root, "")
        elif transversal_type == "levelorder":
            return self.level_order(BT.root)
#           1
#         /  \
#        2     3
#       / \   / \
#      4   5  6  7
#
#
#
    def pre_order(self, start, transversal):
        if start:
            transversal += (str(start.data) + "-")
            transversal = self.pre_order(start.left, transversal)
            transversal = self.pre_order(start.right, transversal)
        return transversal

    def in_order(self, start, transversal):
        if start:
            transversal = self.in_order(start.left, transversal)
            transversal += (str(start.data) + '-')
            transversal = self.in_order(start.right, transversal)
        return transversal

    def post_order(self, start, transversal):
        if start:
            transversal = self.in_order(start.left, transversal)
            transversal = self.in_order(start.right, transversal)
            transversal += (str(start.data) + '-')
        return transversal

    def level_order(self, start):
        queue = Queue()
        queue.enqueue(start)
        traversal = " "
        while len(queue)>0:
            traversal += str(queue.peek()) + '-'
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal


BT = Binary_Tree(1)
BT.root.left = Node(2)
BT.root.right = Node(3)
BT.root.left.left = Node(4)
BT.root.left.right = Node(5)
BT.root.right.left = Node(6)
BT.root.right.right = Node(7)
print(BT.print_transersal('level_order'))

