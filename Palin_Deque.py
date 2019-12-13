class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class deque:
    def __init__(self):
        self.front = self.rear = None

    def addRear(self, item):
        temp = node(item)
        if self.rear is None:
            self.rear = self.front = temp
            return
        self.rear.next = temp
        self.rear = temp

    def addFront(self, item):
        temp = node(item)
        if self.front is None:
            self.rear = self.front = temp
            return
        newnode = temp
        newnode.next = self.front
        self.front = newnode

    def display(self):
        if self.front is None:
            print("empty deque")
        temp = self.front
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def size(self):
        temp = self.front
        count = 0
        while temp.next is not None:
            count += 1
            temp = temp.next
        print("length is: ", count)
        return count

    def removeFront(self):
        if self.front is None:
            print("empty")
        self.front = self.front.next

    def removeRear(self):
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

    def is_Empty(self):
        temp = self.front
        if temp.next == 0:
            print("Empty")

    def reverse(self):
        last = None
        temp = self.front
        while temp.next is not None:
            prev = temp.next
            temp.next = last
            last = temp
            temp = prev
        self.front = last


def palindrome(string):
    rev = string[::-1]
    if string == rev:
        return True
    return False


string = input("enter a string: ")
d = deque()
for word in string:
    d.addRear(word)
d.display()
d.reverse()
d.display()
print(palindrome(string))
