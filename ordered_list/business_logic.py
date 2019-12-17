# *********************************************************************************************************************************************
# @purpose :Implement Ordered list Using LinkedList
# @file    :Ordered_List.py
# @author  :GursheeshKour
# *********************************************************************************************************************************************

#creating a node class
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

#creating a linkedlist class
class linked_list:
    def __init__(self):
        self.head = None

    #creating a method to add data
    def add(self, data):
        new_node = node(data)
        cur_node = self.head
        if self.head is None:
            self.head = new_node
        else:
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = new_node

    
    def size(self):
        cur_node = self.head
        count = 0
        while cur_node is not None:
            count += 1
            cur_node = cur_node.next
        print("length of linked list is: ", count)
        return count

    def search(self, s_word):
        cur_node = self.head
        i = 0
        while cur_node.next is not None:
            if cur_node.data == s_word:
                print(f"element: {s_word} ,is present at an index position: {i} ")
                self.remove(i - 1)
                break
            i += 1
            cur_node = cur_node.next
            print("not present at index position: ", i)

    def remove(self, i):
        if i >= self.size():
            print("error,index out of bound")
            return
        idx = 0
        cur_node1 = self.head
        while True:
            last_node = cur_node1
            cur_node1 = cur_node1.next
            if idx == i:
                last_node.next = cur_node1.next
                return

            idx += 1

    def add_node(self, new_node):
        new_node.next = self.head
        self.head = new_node
        total = self.size()
        total += 1

    def sort(self):
        new_list = []
        cur_node = self.head
        new_list.append(self.head)
        while cur_node.next is not None:
            cur_node = cur_node.next
            new_list.append(cur_node)
            new_list = sorted(new_list, key=lambda node: node.data, reverse=True)
        new_ll = linked_list()
        for node in new_list:
            new_ll.add_node(node)
        return new_ll

    def display(self):
        list1 = []
        cur_node = self.head
        while cur_node is not None:
            list1.append(cur_node.data)
            cur_node = cur_node.next
        print(list1)

    def append(self, data):
        new_node = node(data)
        cur = self.head
        if cur:
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
        else:
            self.head = new_node