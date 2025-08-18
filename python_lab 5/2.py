class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
S1 =Students("Ram", 85)
s2 = Students("Hari", 90)
S3 = Students("Sita", 95)
S1.show_details()
s2.show_details()
S3.show_details()