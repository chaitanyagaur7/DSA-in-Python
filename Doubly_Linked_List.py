'''PYTHON PROGRAM TO MAKE A  DOUBLY LINKED LIST WITH FUNCTIONS :
    1. isEmpty() to return True is linkedlist is Empty
    2. append(v) to insert the value 'v' at the end of the  DOubly linked list
    3. delete_last() to delete the element v from the end of the Doubly linked list
    4. display() to display the content of the Doubly Linked List
'''
#STRUCTURE OF NODE : NONE<-|<-ADDRESS|VALUE|ADDRESS->|<->|<-ADDRESS|VALUE|ADDRESS->|->NONE
#MADE BY CHAITANYA GAUR ON 1st JULY 2023



class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None
class doubly_linked_list:
  def __init__(self):
    self.head = None
    self.last = None
  def isEmpty(self):
      return (self.head == None)
  def append(self,v):
      new_node = Node(v)
      if self.isEmpty():
          self.head = new_node
          self.last = new_node
      else:
          self.last.next = new_node
          new_node.prev = self.last
          self.last = new_node

  def delete_last(self):
      if self.isEmpty():
        return
      elif (self.head == self.last):
          self.head = None
          self.last = None
      else:
          temp = self.last.prev
          self.last = temp
          self.last.next = None
      return

  def display(self):
      if self.isEmpty():
          print("Empty")
      else:
          print(self.head.data)  # Print the data of the head node
          temp = self.head.next
          while temp is not None:
              print(temp.data)
              temp = temp.next

n = Node(5)
l = doubly_linked_list()
l.append(10)
l.append(20)
l.append(30)
l.append(10)
l.append(20)
l.delete_last()
l.display()
