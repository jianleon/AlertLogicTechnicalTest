""" Classes to manage a LinkedList """


class Node:
    """ Class to define a Node object"""

    def __init__(self, info):
        """ Constructor - Node initialization """
        self.info = info
        self.ref = None


class LinkedList:
    """ Class with LinkedList functionality """

    def __init__(self):
        self.root = None

    def add(self, data):
        """ Method to insert a new node in LinkedList

        Parameter
        ---------

        data: object
            Data to insert in LinkedList 

        """
        if self.root == None:
            self.root = Node(data)
        else:
            temp_node = self.root
            while(temp_node):
                if temp_node.ref == None:
                    temp_node.ref = Node(data)
                    return True
                temp_node = temp_node.ref

    def print(self):
        """ Print list """
        temp_list = self.root

        while(temp_list):
            print(temp_list.info)
            temp_list = temp_list.ref

    def detect_loop(self):
        """ Detects if a loop exists in the LinkedList
        
        Return
        ------

        boolean
            True if loop exists

        """
        temp_set = set()
        temp_list = self.root
        while (temp_list):
            if (temp_list in temp_set):
                return True

            temp_set.add(temp_list)
            temp_list = temp_list.ref

        return False


linked_list = LinkedList()

for number in range(10):
    linked_list.add(number)
linked_list.print()

# Creating a loop in list
linked_list.root.ref.ref = linked_list.root

print("Loop found in List!" if linked_list.detect_loop() else "No Loop found")
