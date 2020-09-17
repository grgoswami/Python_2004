
class Student:
    def __init__(self, first_name, last_name, grade, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
        self.gender = gender
        
    def introduce(self, greeting):
        self.greeting = greeting
        print('Hi I am {0} {1}; I go to {2} grade; I am a {3}. {4}'.format(self.first_name,
                                                                self.last_name,
                                                                self.grade,
                                                                self.gender,
                                                                self.greeting))
        
    def re_introduce(self):
        print('Hi! {0}'.format(self.greeting))