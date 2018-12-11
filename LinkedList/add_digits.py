class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def insert(self,value):
        node1 = self
        if node1 is None:
            node1 = Node(value)
        else:
            while node1.next is not None:
                node1 = node1.next
            node = Node(value)
            node1.next = node
            node.next = None
            
    def print_list(self):
        node1 = self
        while node1 is not None:
            print(str(node1.data)+" -> ")
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
    def add(self,n2):
        t1 = self
        t2 = n2
        sum = 0
        head = Node(0)
        carryover = 0
        while t1 is not None and t2 is not None:
            sum = t1.data + t2.data
            if(sum > 9):
                sum = sum % 10
                carryover = sum / 10
            head.insert(sum)
            t1 = t1.next
            t2 = t2.next
        while t1 is not None:
            sum = t1.data + carryover
            if sum > 9 :
                sum = sum % 10
                carryover = sum / 10
            head.insert(sum)
            t1 = t1.next
        while t2 is not None:
            sum = t2.data + carryover
            if sum > 9 :
                sum = sum % 10
                carryover = sum / 10
            head.insert(sum)
            t2 = t2.next
        if head.next is not None:
            head = head.next
        return head
y = 4321+432
n = Node(1)
n.insert(2)
n.insert(3)
n.insert(4)
k = Node(2)
k.insert(3)
k.insert(4)
#n.print_list()
x = n.add(k)
x.print_list()
print (y)
