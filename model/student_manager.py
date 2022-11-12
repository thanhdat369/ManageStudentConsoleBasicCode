class StudentNode:
    def __init__(self, student = None, next=None): 
        self.data = student
        self.next = next

class StudentLinkedList:
    def __init__(self):  
        self.head = None

    def insert_new_student(self, student):
        new_student = StudentNode(student)
        if self.findById(student.id):
            # This condition just for double check
            raise Exception("This student was existed")
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
                current.next = new_student
        else:
            self.head = new_student

    def update_student(self, student_update):
        student = self.findById(student_update.id) 
        if not student: 
            # This condition just for double check
            raise Exception("Can not find student")
        # student.update()

    def findById(self,id):
        current = self.head
        while(current):
            if current.data.id == id:
                return current
            current = current.next
        return None

    # print all linked list
    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next