class Student:
    def __init__(self):
        self.name = "Unknown"
        self.major = "Unknown"
        self.gpa = 0

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = value

    def get_major(self):
        return self.major
    def set_major(self, major):
        self.major = value


    def get_gpa(self):
        return self.gpa
    def set_gpa(self, gpa):
        if 0 <= gpa <= 4.0:
            self.gpa = gpa

    def introduce(self):
        return f"Hi, I'm: {self.name}, I'm studying: {self.major}"

    def study_for_exam(self):
        if self.gpa < 4.0:
            self.gpa += 0.2


student1 = Student()
student1.set_name("Ousman Kandeh")
student1.set_major("Computer Information Technology")
student1.set_gpa(3.5)
student1.study_for_exam()

print(student1.introduce())
print(student1.get_gpa())