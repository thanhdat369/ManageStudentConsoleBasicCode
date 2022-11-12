class StudentNode:
    def __init__(self, student = None, next=None): 
        self.student = student
        self.next = next

class StudentLinkedList:
    def __init__(self):  
        self.head = None

    def insert_new_student(self, student):
        new_student_node = StudentNode(student)
        if self.findStudentById(student.id):
            # This condition just for double check
            raise Exception("This student was existed")
        
        current = self.head
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
                current.next = new_student_node
        else:
            self.head = new_student_node
        return True

    def update_student(self, student_update):
        student = self.findStudentById(student_update.id) 
        if not student: 
            # This condition just for double check
            raise Exception("Can not find student")
        student.update(student_update)
        return True

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
    

    def findStudentById(self,id):
        current = self.head
        while(current):
            if current.student.id == id:
                return current.student
            current = current.next
        return None

    # print all linked list
    def printLL(self):
        current = self.head
        while(current):
            print(current.student)
            current = current.next