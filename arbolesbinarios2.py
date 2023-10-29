class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, value):
        self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.data:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False
        if node.data == value:
            return True
        elif value < node.data:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.data, end=" ")
            self.in_order_traversal(node.right)

    def pre_order_traversal(self, node):
        if node:
            print(node.data, end=" ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.data, end=" ")

# Crear un árbol
tree = BinaryTree(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)

# Ejecutar la búsqueda
print("Búsqueda:")
print("¿Se encuentra 10?", tree.search(10))  # Debería imprimir True
print("¿Se encuentra 7?", tree.search(7))    # Debería imprimir False

# Ejecutar los recorridos
print("\nIn-Order Traversal:")
tree.in_order_traversal(tree.root)
print("\nPre-Order Traversal:")
tree.pre_order_traversal(tree.root)
print("\nPost-Order Traversal:")
tree.post_order_traversal(tree.root)
