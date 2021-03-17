class student:

    def __init__(self, name, topic, grade):  # attaching attributes to every student
        self.name = name
        self.topic = topic
        self.grade = grade


student1 = student("Danny", "Sport", 5)  # object (actual student)
print(student1.name)
