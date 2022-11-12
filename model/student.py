class Student:
    def __init__(self,id,name,address,score) -> None:
        self.id = id 
        self.name = name
        self.address = address
        self.score = score

    def __str__(self) -> str:
        return f"{self.id}-{self.name}-{self.address}-{self.score}"