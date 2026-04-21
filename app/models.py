# This represents how the data will be stored in the database. For now, we will use an in-memory list to store student records. In a real application, you would replace this with actual database models and queries.  

class StudentModel:
    def __init__(self, name: str, age: int, course: str):
        self.name = name
        self.age = age
        self.course = course