## Basic Data Structures
# Arrays
"""
A linear data structure that can hold elements and arrange them. 
Uses contiguous memory space to store elements. 
Can directly access any element based on its index which makes it an EFFICIENT data structure FOR LOOK UPS. 
Arrays have two types: one-dimensional and multi-dimensional.

In Python list() is of type DYNAMIC ARRAY (some langugaes like Java and C++ have both STATIC ARRAYs)
STATIC ARRAYs - have a fixed length - allocates specific memory for that size
DYNAMIC ARRAYs - variable length - allocates specific amount of memory initially. If you need more - allocates 1 new memory capacity (current capacity*2 extra - gets X3 BIGGER EACH TIME) - then moves all elememnts to new area - has OVERHEAD
Data is stored in RAM, not internal storage.
Address of each stored in hexidecimal in RAM

Advantage - 
1) Speed to LOOK UP element BY INDEX
O(1) to look up element by index x e.g. arr[4]

Disadvantage - 
1) Speed to LOOK UP element BY VALUE
O(n) to look up element by specific value x e.g. for i in range(len(arr)): if arr[i] == 207...

2) INSERT/REMOVE new element at specific index e.g. arr.insert(2, 245)
O(n) as all elements after element n need to be shifted 1 down

3) Can have big memory overhead if needed to add 1 value above allocated memory (see note above about x3 memory requirement)

Good if want to store fixed length data and look up often by index but not modify.
"""

#Linked Lists
"""
Addresses a lot of the inefficiencies of Arrays.
A type of data structure used for storing collections of data. 
Data is stored in nodes, each of which contains a data field and a reference (link) to the next node in the sequence. 
Structurally, a linked list is organized into a sequence or chain of nodes. 
Two types of linked lists are commonly used: SINGLY LINKED LISTS, where each node points to the next node and the last node points to null, and DOUBLEY LINKED LISTS, where each node has two links, one to the previous node and another one to the next. 
Used in other types of data structures like STACKS and QUEUES.

Advantage -
1) Fast and memory efficient to add/append another value to end of linked list - just change stored pointed of previous link to inserted one.

"""

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data) -> None:
        """Add node to the end of the linked list."""
        newNode = Node(data)
        # case of empty list
        if self.head == None:
            self.head = newNode
            return  
        
        # traverse linked list
        targetNode = self.head
        while targetNode.next:
            targetNode = targetNode.next
        
        # set next as new node
        targetNode.next = newNode

    def prepend(self, data):
        """Add node to the front of the linked list"""
        newNode = Node(data)
        # case of empty list
        if self.head == None:
            self.head = newNode
            return
        # switch new node and head data
        newNode.next = self.head
        self.head = newNode

    def delete(self, target):
        """Delete node by value"""
        curNode = self.head
        # case of head node is target
        if curNode.data == target:
            self.head = curNode.next
            return 
        
        # track prev node and next node while looking for node
        while curNode.next and curNode.data != target:
            prevNode = curNode
            curNode = curNode.next

        if curNode.data == target:
            prevNode.next = curNode.next
            return 
        else:
            print('Node not found.')


    def printlist(self) -> None:
        """Prints entire linked list"""
        if self.head == None:
            print('Empty List')
            return
        node = self.head
        while node:
            if node.next:
                print(node.data, end = '-->')
            else:
                print(node.data)
            node = node.next
    


# Example Usage:
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.printlist()  # Output: 1 -> 2 -> 3 -> None

ll.prepend(0)
ll.printlist()  # Output: 0 -> 1 -> 2 -> 3 -> None

ll.delete(11)
ll.printlist()  # Output: 0 -> 1 -> 3 -> None

# ll.reverse()
# ll.printlist()  # Output: 3 -> 1 -> 0 -> None

# class Node:
#     def __init__(self, data):
#         self.data = data  # Store data
#         self.next = None  # Pointer to the next node

class LinkedListold:
    def __init__(self):
        self.head = None  

    # Method to insert a new node at the end of the list
    def append(self, data):
        new_node = Node(data)  

        if self.head is None:  # If the list is empty, make the new node the head
            self.head = new_node
            return

        last_node = self.head  # Start at the head of the list
        while last_node.next:  # Traverse to the end of the list
            last_node = last_node.next

        last_node.next = new_node  # Link the last node to the new node

    # Method to insert a new node at the beginning of the list
    def prepend(self, data):
        new_node = Node(data)  # Create a new node with the given data
        new_node.next = self.head  # Link the new node to the current head
        self.head = new_node  # Make the new node the head

    # Method to delete a node by value
    def delete(self, key):
        cur_node = self.head  # Start at the head of the list

        # If the node to be deleted is the head node
        if cur_node and cur_node.data == key:
            self.head = cur_node.next  # Change the head to the next node
            cur_node = None  # Delete the old head
            return

        prev = None
        while cur_node and cur_node.data != key:  # Traverse the list to find the node to delete
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:  # If the key was not found
            return

        prev.next = cur_node.next  # Unlink the node from the list
        cur_node = None  # Delete the node

    # Method to print the linked list
    def print_list(self):
        cur_node = self.head  # Start at the head of the list
        while cur_node:  # Traverse the list
            print(cur_node.data, end=" -> ")  # Print the data
            cur_node = cur_node.next  # Move to the next node
        print("None")

    # Method to reverse the linked list
    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            next_node = cur.next  # Temporarily store the next node
            cur.next = prev  # Reverse the current node's pointer
            prev = cur  # Move the prev and cur one step forward
            cur = next_node
        self.head = prev  # Update the head to the last node

# # Example Usage:
# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.print_list()  # Output: 1 -> 2 -> 3 -> None

# ll.prepend(0)
# ll.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> None

# ll.delete(2)
# ll.print_list()  # Output: 0 -> 1 -> 3 -> None

# ll.reverse()
# ll.print_list()  # Output: 3 -> 1 -> 0 -> None

