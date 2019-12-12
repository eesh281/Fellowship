class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def EnQueue(self, item):
        temp = node(item)
        if self.rear is None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def DeQueue(self):
        if self.is_empty():
            return
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return str(temp.data)

    def display(self):
        if self.front is None:
            print("empty")
        temp = self.front
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def cash_counter(self):
        y = int(input("enter the total number of times you want to deposit or withdraw :"))
        for i in range(y):
            x = int(input("For Deposit enter: 1 and For Withdraw enter2:"))

            if x == 1:

                def deposit():
                    balance = 0
                    num = int(input("enter the number of times to deposit money"))
                    for i in range(num):
                        amount = eval(input("enter the amount"))
                        balance += amount
                        print("total balance is :", balance)
                        q = queue()
                        q.EnQueue(balance)
                        q.display()
                    return balance

                result = deposit()

            elif x == 2:
                print("available balance is", result)
                withdr = eval(input("enter the amount to withdraw"))
                result -= withdr
                print("balance left is :", result)


q = queue()
q.cash_counter()
