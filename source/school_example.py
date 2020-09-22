import os
os.chdir(r'/home/gopi/Python_202004/source')

import school

math = school.Subject('Math', 100)
ela = school.Subject('English', 50)
sci = school.Subject('Science', 50)

st0 = school.Student('Jane', 'Doe', 1, 'girl', [math, ela, sci])
st1 = school.Student('John', 'Doe', 2, 'boy', [math, sci])

st0.introduce('It is nice to meet you.')
st1.introduce('How do you do?')

st0.re_introduce()
st1.re_introduce()

st0.classwork()
st1.classwork()





