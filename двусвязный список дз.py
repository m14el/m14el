class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        current_node = self.head
        if current_node is None:
            self.head = new_node
            return
        while current_node.get_next() is not None:
            current_node = current_node.get_next()
        current_node.set_next(new_node)

    def show(self):
        current_node = self.head
        output = ""
        while current_node is not None:
            output += str(current_node.get_data())
            current_node = current_node.get_next()
        print(output, end=' ')

    def length(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.get_next()
        print(count)

    def push_front(self, data):
        new_node = Node(data)
        current_node = self.head
        new_node.set_next(current_node)
        self.head = new_node

    def remove_back(self):
        current_node = self.head
        while current_node.get_next().get_next() is not None:
            current_node = current_node.get_next()
        current_node.set_next(None)

    def remove_front(self):
        current_node = self.head
        self.head = current_node.get_next()

    def value_at(self, index):
        current_node = self.head
        count = 0
        while current_node is not None:
            if count == index:
                return current_node.get_data()
            count += 1
            current_node = current_node.get_next()
        print('Index is out of range')

    def insert(self, index, data):
        new_node = Node(data)
        current_node = self.head
        count = 0
        while current_node.get_next() is not None:
            if index == 0:
                self.push_front(data)
                return
            if count + 1 == index:
                node_after_current = current_node.get_next()
                current_node.set_next(new_node)
                new_node.set_next(node_after_current)
                return
            count += 1
            current_node = current_node.get_next()
        print('Index is out of range')

    def remove(self, index):
        current_node = self.head
        count = 0
        while current_node.get_next() is not None:
            if index == 0:
                self.remove_front()
                return
            if count + 1 == index:
                node_to_remove = current_node.get_next()
                node_after_remove = node_to_remove.get_next()
                current_node.set_next(node_after_remove)
                return
            count += 1
            current_node = current_node.get_next()
        print('Index is out of range')

    def reverse_(self):
        previous = None
        current_node = self.head
        next = None
        while current_node is not None:
            next = current_node.get_next()  # выбираем следующее
            current_node.set_next(previous)  # следующим делаем предыдущее
            previous = current_node  # предыдущее сдвигаем на текущее
            current_node = next  # а текущее передвигаем на следующее
        self.head = previous


my_list = LinkedList()
my_list.append(2)
my_list.append(4)
my_list.append(8)
my_list.append(16)

# my_list.show()
# my_list.push_front(56)
# my_list.show()
# print(my_list.value_at(2))
# my_list.length()
# my_list.show()
# my_list.remove_back()
# my_list.show()
# my_list.remove_front()
# my_list.show()
# my_list.insert(2, 15)
# my_list.show()
my_list.remove(1)
my_list.show()
my_list.reverse_()
my_list.show()