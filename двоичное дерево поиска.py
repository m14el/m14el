class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None
        self.parent = None


class BinarySearchTree:
    def __init__(self):
        self.self = Node()

    def add(self, value):
        if self.self.value is None:
            self.self.value = value
            return
        self.add_data(self.self, value)

    def add_data(self, cn, value):  # cn - current node
        if cn.value > value:
            if cn.left is None:
                cn.left = Node()
                cn.left.value = value
                cn.left.parent = cn
            else:
                self.add_data(cn.left, value)
        else:
            if cn.right is None:
                cn.right = Node()
                cn.right.value = value
                cn.right.parent = cn
            else:
                self.add_data(cn.right, value)

    def find(self, value):
        if self.self.value is None:
            return False

        if self.self.value == value:
            return True

        node = self.find_node(self.self, value)
        if node is None:
            return False

        return True

    def find_node(self, cn, value):
        if cn is None:
            return None

        if cn.value == value:
            return cn

        if cn.value > value:
            res = self.find_node(cn.left, value)
            return res
        else:
            res = self.find_node(cn.right, value)
            return res

    def find_min(self):
        node = self.find_min_node(self.self)
        return node.value

    def find_min_node(self, cn):
        if cn.left is None:
            return cn

        node = self.find_min_node(cn.left)
        return node

    def find_max(self):
        node = self.find_max_node(self.self)
        return node.value

    def find_max_node(self, cn):
        if cn.right is None:
            return cn

        node = self.find_max_node(cn.right)
        return node

    def delete(self, value):
        if (self.self.left is None and
                self.self.right is None and
                self.self.value == value):
            self.self.value = None
            return

        if (self.self.left is not None and
                self.self.right is None and
                self.self.value == value):
            self.self = self.self.left
            self.self.parent = None
            return

        if (self.self.left is None and
                self.self.right is not None and
                self.self.value == value):
            self.self = self.self.right
            self.self.parent = None
            return

        node = self.find_node(self.self, value)
        if node is None:
            raise Exception('No such node for delete')
        self.delete_data(node)

    def delete_data(self, node):
        # если нет детей
        if (node.left is None and node.right is None):
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right == None

            return

        # если дети есть

        # если 1 (левый) ребенок
        if (node.left is not None and node.right is None):
            if node.parent.left == node:
                node.parent.left = node.left
            else:
                node.parent.right = node.left
            return

        # если 1 (правый) ребенок
        if (node.left is None and node.right is not None):
            if node.parent.left == node:
                node.parent.left = node.right
            else:
                node.parent.right = node.right
            return

        # если 2 детей
        if (node.left is not None and node.right is not None):
            min_node_of_right = self.find_min_node(node.right)
            min_node_of_right.left = node.left
            if node.parent.left == node:
                node.parent.left = min_node_of_right
            else:
                node.parent.right = min_node_of_right
            return
        # если 2 детей
        raise Exception('Something went wrong. Can\'t delete a node')

    def remove_self_with_two_children(self):
        if self is None:
            return None

        # Если корень имеет двух потомков
        if self.left is not None and self.right is not None:
            # Находим самый правый узел в левом поддереве
            max_left = self.left
            while max_left.right is not None:
                max_left = max_left.right

            # Заменяем значение корня на значение самого правого узла в левом поддереве
            self.value = max_left.value

            # Рекурсивно удаляем самый правый узел из левого поддерева
            self.left = (self.left, max_left.value)

        return self

    def remove_node(self, value):
        if self is None:
            return None

        if value < self.value:
            self.left = (self.left.value)
        elif value > self.value:
            self.right = (self.right.value)
        else:
            # Если узел не имеет потомков или имеет только одного потомка
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                # Узел имеет двух потомков
                # Находим самый правый узел в левом поддереве
                max_left = self.left
                while max_left.right is not None:
                    max_left = max_left.right

                # Заменяем значение удаляемого узла на значение самого правого узла в левом поддереве
                self.value = max_left.value

                # Рекурсивно удаляем самый правый узел из левого поддерева
                self.left = (self.left, max_left.value)

        return self


bst = BinarySearchTree()
print(bst.find(10), bst.find(8), bst.find(20))
bst.add(10)
print(bst.find(10), bst.find(8), bst.find(20))
bst.add(8)
print(bst.find(10), bst.find(8), bst.find(20))
bst.add(9)
print(bst.find(10), bst.find(8), bst.find(20))
bst.add(7)
print(bst.find(10), bst.find(8), bst.find(20))
bst.add(20)
print(bst.find(10), bst.find(8), bst.find(20))

print(bst.find_min(), bst.find_max())

bst = BinarySearchTree()
bst.add(5)
bst.add(3)
bst.add(1)
bst.add(2)
bst.add(8)
bst.add(7)
bst.add(6)
bst.add(19)
bst.add(15)
bst.add(22)

bst.delete(2)
bst.delete(15)
bst.delete(22)
