'''PYTHON PROGRAM TO MAKE A LINKED LIST WITH FUNCTIONS :
    1. isEmpty() to return True is linkedlist is Empty
    2. append(v) to insert the value 'v' at the end of the linkedlist
    3. delete(v) to delete the element v from the linked list
    4. reverse() to reverse the linked list
    5. display() to display the content of the Doubly Linked List
'''
#STRUCTURE OF NODE : |VALUE|ADDRESS->|->|VALUE|ADDRESS->|->NONE
#MADE BY CHAITANYA GAUR ON 1st JULY 2023

class Node:
    def __init__(self,v = None):
        self.value = v
        self.next = None
        return
    def isEmpty(self):
        return (self.value == None)
    def append(self,v):
        if self.isEmpty():
            self.value = v
            self.next = None
        elif (self.next == None):
            self.next = Node(v)
        else:
            temp = self
            while (temp.next !=None):
                temp = temp.next
            temp.next = Node(v)
        return

    def delete(self, v):
        if self.isEmpty():
            return "The list is empty"
        elif self.value == v:
            self.value = None
            self.next = None
            return "This was the last element, now it's an empty list"
        else:
            temp = self
            temp1 = None
            while temp and temp.value != v:
                temp1 = temp
                temp = temp.next
            if temp:
                temp1.next = temp.next
            else:
                return "Element not found"

    def display(self):
        if self.isEmpty():
            print("The Linked List is Empty")
            return
        temp = self
        while (temp.next!=None):
            print(temp.value,end = "--->")
            temp = temp.next
        print(temp.value)
        return

    def reverse(self):
        if self.isEmpty():
            return
        elif self.next == None :
            return self
        else:
            temp = self
            temp1 = None
            while (temp != None):
                temp2 = temp.next
                temp.next = temp1
                temp1 = temp
                temp = temp2
          #      temp = temp.next
            return temp1




head = Node(10)
head.append(20)
head.append(30)
head.append(20)
head.append(30)
head = head.reverse()
head.display()

