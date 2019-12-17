# *********************************************************************************************************************************************
# @purpose :Creating a util Class Using LinkedList
# @file    :utility.py
# @author  :GursheeshKour
# *********************************************************************************************************************************************

#creating a node class
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

#creating a linkedlist class
class Linked_List:
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

    #creating a method to check size
    def size(self):
        cur_node = self.head
        count = 0
        while cur_node is not None:
            count += 1
            cur_node = cur_node.next
        print("length of linked list is: ", count)
        return count

    #creating a method to search a word
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

    #creating a method to remove an element from specific position
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

    #creating a method to create a node
    def add_node(self, new_node):
        new_node.next = self.head
        self.head = new_node
        total = self.size()
        total += 1

    #creating a method to sort the linkedlist
    def sort(self):
        new_list = []
        cur_node = self.head
        new_list.append(self.head)
        while cur_node.next is not None:
            cur_node = cur_node.next
            new_list.append(cur_node)
            new_list = sorted(new_list, key=lambda node: node.data, reverse=True)
        new_ll = Linked_List()
        for node in new_list:
            new_ll.add_node(node)
        return new_ll

    #creating a method to display a linkedlist
    def display(self):
        list1 = []
        cur_node = self.head
        while cur_node is not None:
            list1.append(cur_node.data)
            cur_node = cur_node.next
        print(list1)

    #creating a method to append data to linkedlist
    def append(self, data):
        new_node = node(data)
        cur = self.head
        if cur:
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
        else:
            self.head = new_node

    #creating a method to check whether the list is empty or not
    def isEmpty(self):
        cur_node = self.head
        if cur_node.next == 0:
            print("linked list is empty")
        print("linked list has data")


#*****************************************************************************************************


#creating a class for the queue 
class Queue:
    #initialising the constructor
    def __init__(self):
        self.front = self.rear = None

    #creating a method to check whether the linkedlist is empty or not
    def is_empty(self):
        return self.front is None

    #creating a method to add an element to the queue from rear
    def enqueue(self, item):
        temp = node(item)
        if self.rear is None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    #creating a method to delete an element from queue from front
    def dequeue(self):
        if self.is_empty():
            return
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return str(temp.data)

    #creating a method to display a linkedlist
    def display(self):
        if self.front is None:
            print("empty")
        temp = self.front
        while temp is not None:
            print(temp.data)
            temp = temp.next


# *********************************************************************************************************************************************


#creating a class for deque
class Deque:
    #initialising the constructor
    def __init__(self):
        self.front = self.rear = None

    #method to add element from rear
    def addfear(self, item):
        temp = node(item)
        if self.rear is None:
            self.rear = self.front = temp
            return
        self.rear.next = temp
        self.rear = temp

    #method to add element from front
    def addfront(self, item):
        temp = node(item)
        if self.front is None:
            self.rear = self.front = temp
            return
        newnode = temp
        newnode.next = self.front
        self.front = newnode

    #method to display a linked list 
    def display(self):
        if self.front is None:
            print("empty deque")
        temp = self.front
        while temp is not None:
            print(temp.data)
            temp = temp.next

    #method to check size of linkedlist
    def size(self):
        temp = self.front
        count = 0
        while temp.next is not None:
            count += 1
            temp = temp.next
        print("length is: ", count)
        return count

    #method to remove element from front
    def remove_front(self):
        if self.front is None:
            print("empty")
        self.front = self.front.next

    #method to remove element from rear
    def remove_rear(self):
        if self.front is None:
            print("empty")
        if self.front.next is None:
            self.front = None
            return None
        second_last = self.front
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None
        return self.front

    #method to check whether list is empty or not
    def is_Empty(self):
        temp = self.front
        if temp.next == 0:
            print("Empty")

    #method to reverse the string
    def reverse(self):
        last = None
        temp = self.front
        while temp.next is not None:
            prev = temp.next
            temp.next = last
            last = temp
            temp = prev
        self.front = last


#*****************************************************************************************************