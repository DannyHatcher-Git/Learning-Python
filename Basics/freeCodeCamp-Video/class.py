class student:

    def __init__(self, name, topic, grade):  # attaching attributes to every student
        self.name = name
        self.topic = topic
        self.grade = grade

    def on_grade(self):  # Making a function inside a class
        if self.grade >= 3:  # If the student chose has a grade higher than 3
            return True
        else:
            return False


student1 = student("Danny", "Sport", 5)  # object (actual student)
print(student1.name)
print(student1.on_grade())  # Using the fucntion inside a class
