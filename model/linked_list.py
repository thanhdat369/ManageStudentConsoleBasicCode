class StudentNode:
  def __init__(self, student = None, next=None): 
    self.data = student
    self.next = next

class StudentLinkedList:
  def __init__(self):  
    self.head = None
  
  def insert(self, data):
    newNode = StudentNode(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
  # print method for the linked list
  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next