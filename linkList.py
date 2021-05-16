#creat a Node calss
class Node:
    def __init__(self,data):
        self.position=data
        self.next_reference =None
        self.previous_reference = None

#creat a doubly link list class
class DoublyLinkedlist:
    def __init__(self):
        self.head_node = None

    # inserting to a empty list if first node is empty
    def insert_in_emptylist(self,data):
        if self.head_node is None:
            new_node = Node(data)
            self.head_node = new_node
        else:
            print("list is not empty")
#insertion
    #insert a node at front of the intance
    def insert_at_front(self,data):
        if self.head_node is None:
            new_node = Node(data)
            self.head_node = new_node
            print("head node is inserted")
            return
        new_node = Node(data)
        new_node.next_reference = self.head_node
        self.head_node.previous_reference = new_node
        self.head_node = new_node

    #insert a node at end of the instence
    def insert_at_end(self,data):
        if self.head_node is None:
            new_node = Node(data)
            self.head_node = new_node
            return
        node = self.head_node
        while node.next_reference is not None:
            node = node.next_reference
        new_node = Node(data)
        node.next_reference = new_node
        new_node.previous_reference = node

    # insert a Node given position
    # insert a node after the given position
    def insert_after_position(self,x,data):
        if self.head_node is None:
            print("This is a empty List")
            return
        else:
            node = self.head_node
            while node is not None:
                if node.position == x:
                    break
                node = node.next_reference
            if node is None:
                print("This position is not in the list")
            else:
                new_node = Node(data)
                new_node.previous_reference = node
                new_node.next_reference = node.next_reference
                if node.next_reference is not None:
                    node.next_reference.previous_reference = new_node
                node.next_reference = new_node

    # inert a node before the given position
    def insert_before_position(self , x , data):
        if self.head_node is None:
            print("This list is empty")
            return
        else:
            node = self.head_node
            while node is not None:
                if node.position == x:
                    break
                node = node.next_reference
            if node is None:
                print("This position is not in the list")
            else:
                new_node = Node(data)
                new_node.next_reference = node
                new_node.previous_reference = node.previous_reference
                if node.previous_reference is not None:
                    node.previous_reference.next_reference = new_node
                node.previous_reference = new_node

#deletion
    #delete a node at front of the instance
    def delete_at_front(self):
        if self.head_node is None:
            print("This list has no elements to delete ")
            return
        if self.head_node.next_reference is None:
            self.head_node = None
            return
        self.head_node = self.head_node.next_reference
        self.head_node.prev = None

    #delete a node at end of the instance
    def delete_at_end(self):
        if self.head_node is None:
            print("This list has no elements to delete")
            return
        if self.head_node.next_reference is None:
            self.head_node = None
            return
        node = self.head_node
        while node.next_reference is not None:
            node = node.next_reference
        node.previous_reference.next_reference = None

    # delete a node when given position of the instance
    def delete_when_given_poss(self,x):
        if self.head_node is None:
            print("This list has no elements to delete")
            return
        if self.head_node.next_reference is None:
            if self.head_node.position == x:
                self.head_node = None
            else:
                print("position not found")
            return

        if self.head_node.position == x:
            self.head_node = self.head_node.next_reference
            self.head_node.previous_reference = None
            return

        node = self.head_node
        while node.next_reference is not None:
            if node.position == x:
                break;
            node = node.next_reference
        if node.next_reference is not None:
            node.previous_reference.next_reference = node.next_reference
            node.next_reference.previous_reference = node.previous_reference
        else:
            if node.position == x:
                node.previous_reference.next_reference = None
            else:
                print("position not found")

# traversing
    # traversing forward along the list
    def traverse_forward(self):
        if self.head_node is None:
            print("List has no element")
            return
        else:
            node = self.head_node
            while node is not None:
                print(node.position," ")
                node = node.next_reference

    # traversing backward along the list
    def traverse_backward(self):
        if self.head_node is None:
            print("This list has no element to delete")
            return
        node = self.head_node
        reverse = node.next_reference
        node.next_reference = None
        node.previous_reference = reverse
        while reverse is not None:
            reverse.previous_reference = reverse.next_reference
            reverse.next_reference = node
            node = reverse
            reverse = reverse.previous_reference
        self.head_node = node

    # searching for the given with printing the position of the node.
    def search_list(self, x):
        z = 1;
        f = False;
        node = self.head_node;

        if self.head_node == None:
            print(" This list is empty")
            return ;
        while node != None:
            if node.position == x:
                f = True;
                break;
            node = node.next_reference;
            z = z+1;
        if f:
            print(">>Node is present in the list at the position: "+ str(z));
        else:
            print(">>Node is not present in the list ");


# creat objects
new_link_list = DoublyLinkedlist()

# insert to empty list
new_link_list.insert_in_emptylist(1)
# insert to front
new_link_list.insert_at_front(10)
new_link_list.insert_at_front(100)
new_link_list.insert_at_front(1000)
# insert to end
new_link_list.insert_at_end(20)
new_link_list.insert_at_end(200)
new_link_list.insert_at_end(2000)
# insert after the given pos
new_link_list.insert_after_position(1,0)
# insert before the given pos
new_link_list.insert_before_position(1,0)

# delete first node
'''new_link_list.delete_at_front()''' # remove comment type and run
# delete last node
'''new_link_list.delete_at_end()''' # remove comment type and run
# delete node when given pos
'''new_link_list.delete_when_given_poss(1)''' # remove comment type and run
# search the list
new_link_list.search_list(10)
new_link_list.search_list(360)
new_link_list.search_list(0)

# travel backward
'''new_link_list.traverse_backward()''' # remove comment type and run
# travel forward
new_link_list.traverse_forward()




























































































