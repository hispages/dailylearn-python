class Student:
    def __init__(self, name, student_id, scores):
        self.name = name
        self.student_id = student_id
        self.scores = scores

    def datalist(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Score: {self.scores}")
        print(f"grade: {self.calculategrade()}")

    def calculategrade(self):
        if self.scores >=85 :
            return "A"
        
        elif self.scores >=70 :
            return "B"
        
        elif self.scores >=55 :
            return "C"
        
        elif self.scores >=40 :
            return "D"

        else:
            return "E"


class Studentlist:
    def __init__(self):
        self.list = []

    def AddnewStudent(self, student):
        self.list.append(student)
    
    def all_listOfstudent(self):
        for student in self.list:
            print("______________")
            student.datalist()

    def find_student(self, put):
        for student in self.list:
        
            if student.name == put:
                return student
            elif student.student_id == put:
                return student
        return None
    
    #def find_id(self, student_id):
        for student in self.list:
        
            if student.student_id == student_id:
                return student
        return None
    
    def new_scores(self, put, Score_update):
        student = self.find_student(put)
        if student:
            student.scores = Score_update
            return True
        elif student:
            student.scores = Score_update
            return True
        return False
    
    #def new_scores(self, name, Score_update):
        student = self.find_id(name)
        if student:
            student.scores = Score_update
            return True
        return False
    
    def remove_student(self, Remove):
        for student in self.list:
            if student.student_id == Remove:
                self.list.remove(student)
                return True
            elif student.name == Remove:
                self.list.remove(student)
                return True
        return False
        
   # def remove_id(self, name):
        for student in self.list:
            if student.name == name:
                self.list.remove(student)
                return True
        return False