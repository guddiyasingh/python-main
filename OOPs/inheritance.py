class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I'm {self.name}"


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def greet(self):
        return f"{super().greet()} and I'm a student (ID: {self.student_id})"


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def greet(self):
        return f"{super().greet()} and I teach {self.subject}"


# Multiple inheritance example
class Researcher:
    def research(self):
        return "Doing research"


class Professor(Teacher, Researcher):
    pass


def show():
    people = [Person("Alex"), Student("Bella", 123), Teacher("Carlos", "Math"), Professor("Dana","Physics")]
    for p in people:
        print(f"{p.__class__.__name__}: {p.greet()}")

    # Professor inherits research() from Researcher
    prof = Professor("Eve", "Computer Science")
    print(f"Professor research: {prof.research()}")


if __name__ == "__main__":
    show()
