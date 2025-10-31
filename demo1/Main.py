from IPython.terminal.shortcuts.auto_suggest import accept

from demo1.Student import Students


def menu():
    print("-----------------------------------------")
    print("0. EXIT")
    print("1. Add Students")
    print("2. Display All Students")
    print("3. Sort Students by Name")
    print("4. Sort Students by Roll number")
    print("5. Sort Students by Marks")
    print("-----------------------------------------")
    choice=input("Enter Your Choice: ")
    print("-----------------------------------------")

    return choice


Students=[5]

print("Welcome to Students Data Base")
while True:
    choice=menu()
    match choice:
        case "1":
            s = Students()
            s.accept()
            Students.append(s)


