class Student:
    def __init__(self,id,name,address,score) -> None:
        self.id = id 
        self.name = name
        self.address = address
        self.score = score

    def update(self,update_student):
        if self.id != update_student.id:
            raise Exception("Can not update different ID")
        self.name = update_student.name
        self.address = update_student.address
        self.score = update_student.score

    def __str__(self) -> str:
        return f"{self.id}-{self.name}-{self.address}-{self.score}"+\
                "\n------------------------"