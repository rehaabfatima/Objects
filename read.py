class student:
    name="penguin"
    grade=10

    def intro(self):
        print("Hi I am a student")

    def details(self):
        print("my name is ",self.name)
        print("I am in grade",self.grade)


ob=student()
ob.intro()
ob.details()