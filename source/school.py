import sys

class Student:
    def __init__(self, first_name, last_name, grade, gender, subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
        self.gender = gender
        self.subjects = subjects
        if len(self.subjects) == 0:
            print('The student has to take at least one subject')
            sys.exit(1)
        
    def introduce(self, greeting):
        self.greeting = greeting
        print('Hi I am {0} {1}; I go to {2} grade; I am a {3}. {4}'.format(self.first_name,
                                                                self.last_name,
                                                                self.grade,
                                                                self.gender,
                                                                self.greeting))
        
    def re_introduce(self):
        print('Hi! {0}'.format(self.greeting))
        
    def classwork(self):
        print('This student is taking the following subjects:')
        for sub in self.subjects:
            sub.describe()              

class Subject:
    def __init__(self, name, points):
        self.name = name
        self.points = points
        
    def describe(self):
        print('This is: subject={0}, points={1}'.format(self.name, self.points))
        
        
    