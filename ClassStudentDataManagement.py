class student:
    def __init__(self, name, student_id, scores):
        self.name = name
        self.student_id = student_id
        self.scores = scores

    def datalist(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Score: {self.scores}")

    def calculategrade(self):
        if self.nilai >=85 :
            return "A"
        
        elif self.nilai >=70 :
            return "B"
        
        elif self.nilai >=55 :
            return "D"
        
        elif self.nilai >=40 :
            return "c"
        
        else:
            return "E"
        

class Studentlist:
    def __init__(self):
        self.list =[]

    def AddnewStudent(self, student):
        self.list.append(student)
    
    def all_listOfstudent(self):
        for stundet in self.list:
            print("______________")
            student.datalist