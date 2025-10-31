class Students:
    def __init__(self,name,rollNO,marks):
        self.name=name
        self.rollNo=rollNO
        self.marks=marks

    def __str__(self):
        return f"Name: {self.name}, Roll No: {self.rollNo}, Marks: {self.marks}"

    def accept(self):
        print("Enter you Details")
        self.name=input("Enter your Name: ")
        self.rollNo=input("Enter your Roll No: ")
        self.marks=input("Enter your Marks: ")
