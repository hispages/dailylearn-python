from ClassStudentDataManagement import Student
from ClassStudentDataManagement import Studentlist

#student1.datalist()
#print("______________")
#student2.datalist()

student1 = Student("Lia", "2191247", 97)
student2 = Student("kadin", "3218312", 56)
student3 = Student("riski", "4320847", 44)




dataa = Studentlist()

dataa.AddnewStudent(student1)
dataa.AddnewStudent(student2)
dataa.AddnewStudent(student3)

# you can also can type this way for more efficiency
dataa.AddnewStudent(Student("Citra", "11223344", 75))


# to show all student you can run this " dataa.all_listOfstudent "


# you can find student Name/id by filling the string with name or id \/
# example.

#find = dataa.find_student("")
#if find:
#    find.datalist()

# here you can remove certain student by filling the string with name or id
# example.

#dataa.remove_student("")

# here you can update student scores by filling the string and put new score after the comma (,)
# example.

#dataa.new_scores("", )



dataa.all_listOfstudent()