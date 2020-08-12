class Binary_Search_Tree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def add_node(self, data):

        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_node(data)
            else:
                self.left = Binary_Search_Tree(data)
        else:
            if self.right:
                self.right.add_node(data)
            else:
                self.right = Binary_Search_Tree(data)

    def in_order_transversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_transversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_transversal()

        return elements

    def pre_order_transversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.in_order_transversal()
        if self.right:
            elements += self.right.in_order_transversal()
        return elements

    def post_order_transversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_transversal()
        if self.right:
            elements += self.right.in_order_transversal()
        elements.append(self.data)
        return elements

    def search(self, value):
        if value == self.data:
            return True
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self, value):
        if value < self.data:
            if self.left:
               self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right.delete(value)

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self


def build_tree(elements):
    root = Binary_Search_Tree(elements[0])
    for i in range(1,len(elements)):
        root.add_node(elements[i])
    return root

if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,18,34]
    numbers_tree = build_tree(numbers)
    numbers_tree.delete(20)
    print(numbers_tree.pre_order_transversal())
