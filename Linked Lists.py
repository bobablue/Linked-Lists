# Singly linked list 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return(str(self.data))


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None

        # create head of linked list
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node

            # link all subsequent elements after head
            for i in nodes:
                node.next = Node(i)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return(" -> ".join([str(i) for i in nodes]))

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __getitem__(self, index):
        length = self.length()
        neg_index = {-k:v for k,v in zip(range(1,length+1),reversed(range(length)))}
        if index<0 and index in neg_index.keys():
            index = neg_index[index]

        count = 0
        for node in self:
            if count==index:
                return(node.data)
            count = count+1
        raise Exception(f'Index {index} is out of range')

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return

        # have to iterate through the whole linked list to reach last node, before adding new node
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data==target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(f'Node with data {target_node_data} not found')

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data==target_node_data:
            return(self.add_first(new_node))

        prev_node = self.head
        for node in self:
            if node.data==target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception(f'Node with data {target_node_data} not found')

    def remove_node(self, target_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data==target_node:
            self.head = self.head.next
            return

        prev_node = self.head
        for node in self:
            if node.data==target_node:
                prev_node.next = node.next
                return
            prev_node = node

        raise Exception(f'Node with data {target_node_data} not found')

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def length(self):
        count = 0
        for node in self:
            count = count+1
        return(count)


llist = LinkedList([1,2,3])
print(llist)

llist = LinkedList([1,2,3])
for i in llist:
    print(i)

llist = LinkedList([1,2,3])
print(llist[0], llist[-1])

llist = LinkedList([1,2,3])
print(llist)
llist.add_first(Node(0))
print(llist)

llist = LinkedList([1,2,3])
print(llist)
llist.add_last(Node(4))
print(llist)

llist = LinkedList([1,2,3])
print(llist)
llist.add_after(2,Node(2.5))
print(llist)

llist = LinkedList([1,2,3])
print(llist)
llist.add_before(2,Node(1.5))
print(llist)

llist = LinkedList([1,2,3])
print(llist)
llist.remove_node(1)
print(llist)

llist = LinkedList([1,2,3])
print(llist)
llist.reverse()
print(llist)

llist = LinkedList([1,2,3])
llist.length()
