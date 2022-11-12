class StudentNode:
    def __init__(self, student = None, next=None): 
        self.student = student
        self.next = next

class StudentLinkedList:
    def __init__(self):  
        self.head = None

    def insert_new_student(self, student):
        new_student_node = StudentNode(student)
        if self.findById(student.id):
            # This condition just for double check
            raise Exception("This student was existed")
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
                current.next = new_student_node
        else:
            self.head = new_student_node

    def update_student(self, student_update):
        student_node = self.findById(student_update.id) 
        if not student_node: 
            # This condition just for double check
            raise Exception("Can not find student")
        student_node.student.update(student_update)

    def delete_student(self, id):
        current = self.head
        if (not current):
            if (current.student.id == id):
                self.head = current.next
                current = None
                return True
 
        while (current):
            if current.data.id == id:
                break
            prev = temp
            temp = temp.next
 
        if(not current):
            return False
         
        prev.next = temp.next
        current = None
        return True
    

    def findById(self,id):
        current = self.head
        while(current):
            if current.student.id == id:
                return current
            current = current.next
        return None

    # print all linked list
    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next