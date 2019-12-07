class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None

    def display(self):
        list1 = []
        current_node1 = self.head
        while current_node1.next is not None:
            list1.append(current_node1.data)
            current_node1 = current_node1.next
        print(list1)

    def add(self, data):
        new_node = node(data)
        current = self.head
        if self.head is None:
            self.head = new_node
        else:
            while current.next is not None:
                current = current.next
            current.next = new_node
        return

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def size(self):
        cur_node = self.head
        count = 0
        while cur_node != None:
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
            print("not present at index position: ",i)

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

    def isEmpty(self):
        cur_node = self.head
        if cur_node.next == 0:
            print("linked list is empty")
        print("linked list has data")


def open_file():
    i = 0
    f = open("text_file.txt", "r+")
    line = f.read()
    li = linked_list()
    for word in line.split(" "):
        li.add(word)
        i += 1

    li.display()
    li.isEmpty()
    li.size()
    s_word = input("enter a word to search: ")
    li.search(s_word)
    li.append(s_word)
    li.append(s_word)
    li.display()
    f.write(str(s_word))
    f.close()
open_file()
