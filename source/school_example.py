import os
os.chdir(r'C:\Users\Gia\Documents\Python_202004')

import school

st0 = school.Student('Jane', 'Doe', 1, 'girl')
st1 = school.Student('John', 'Doe', 2, 'boy')

st0.introduce('It is nice to meet you.')
st1.introduce('How do you do?')

st0.re_introduce()
st1.re_introduce()



