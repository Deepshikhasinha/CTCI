class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def insert(self,value):
        node1 = self
        while node1.next is not None:
            node1 = node1.next
        node = Node(value)
        node1.next = node
        node.next = None
            
    def print_list(self):
        node1 = self
        while node1 is not None:
            print(str(node1.data)+" -> "),
            node1 = node1.next
    def n_to_last(self, n):
        n1 = self
        n2 = self
        count = 0
        while n2.next is not None:
            if count >= n:
                n1 = n1.next
            count += 1
            n2 = n2.next
        return n1.data

n = Node(1)
n.insert(6)
n.insert(5)
n.insert(3)
n.insert(8)
n.print_list()
x = n.n_to_last(4)
print("\n"+str(x))
