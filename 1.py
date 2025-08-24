class Student:
    def __init__(self,name,roll_no,*marks):
        self.name = name
        self.roll_no = roll_no
        self.marks =marks
    def __str__(self):
        return f'name of student: {self.name}, roll number: {self.roll_no}, marks obtained: {self.marks}'
    def display(self,):
        n = len(self.marks)
        print(f"name of student: {self.name}")
        print(f"roll number : {self.roll_no}")
        print(f"marks obtained in {n} subject: {self.marks}")
ob1 = Student("Ram",36,98,96,95,94)
ob2 =ob1.display()