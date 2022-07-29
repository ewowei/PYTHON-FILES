"""
 LINKED LIST - DATA STRUCTURE 
 What is LinkedList? 
 A linked List is a data structure used for storing collections of data. A linked list has the following properties.
 
• Successive elements a re connected by pointers
• The last element points to NULL
• Can grow or shrink in size during execution of a program
• Can be made just as long as required (until systems memory exhausts)
• Docs not waste memory space (but takes some extra memory for pointers) 
"""
# Create a NODE
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

# Create the Linked_list
class Linked_list:
    def __init__(self):
        self.head = None

    def print_data(self):
        n = self.head
        while n!= None:
            print(n.data, end='-->')
            n = n.ref

# Adding Node at the beginning of LinkedList
    def Add_begin(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.ref = self.head
            self.head = new_node

# Adding Node at the END of LinkedList
    def Add__at_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.ref!= None:
                n = n.ref
            n.ref = new_node

# Adding Node before a given data(Node) of LinkedList
    def Before_given(self, data, x):
        n = self.head
        while n.ref!= None:
            if n.ref.data == x:
                break
            n = n.ref
        if self.head == None:
            print("Empty List")
            return
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

# Adding Node After a given data(Node) of LinkedList
    def After_given(self, data, x):
        n = self.head
        if self.head ==None:
            print('Empty List')
            return
        else:
            new_node =  Node(data)
            while n.ref!=None:
                if n.data == x:
                    break
                n = n.ref
            new_node.ref = n.ref
            n.ref = new_node

# Delete the first ELEMENT of the Linkedlist

    def delete_start(self):
        if self.head == None:
            print("List is empty, nothing to delete")
            return
        else:
            self.head = self.head.ref

# Delete the LAST ELEMENT of the Linkedlist
    def delete_End(self):
        n = self.head
        while n.ref!=None:
            if n.ref.ref == None:
                break
            n = n.ref
        n.ref = None

    def delete_given(self, data):
        n = self.head
        if n == None:
            print('List is empty')
            return
        if self.head.data == data:
            self.head = self.head.ref
        while n.ref.ref!=None:
            if n.ref.data == data:
                break
            n = n.ref
        if n.ref == None:
            print('Node not present')
        else:
            n.ref = n.ref.ref


link = Linked_list()
link.Add_begin(10)
link.Add_begin(20)
link.Add_begin(80)
link.delete_given(80)

link.print_data()





