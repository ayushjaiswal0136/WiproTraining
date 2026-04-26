from oops.college import College
from oops.student import Student

cc = int(input(' Coll Code: '))
cn = input('Coll Name: ')
ci = input('City : ')
rno = int(input('Roll no'))
sn = input('stu name')
m1 = int(input('Marks 1'))
m2 = int(input('Marks 2'))
m3 = int(input('Marks 3'))

#project = College(ccode = cc, cname = cn, ccity = ci)

#project.welcome_message()
#project.display_college_details()


project  = Student(ccode = cc, cname=cn, ccity=cc,
                   rno = rno, sname=sn, m1=m1, m2=m2, m3=m3)

project.welcome_message()
project.display_college_details()
print(f'Roll no: {project.rollno} \t Name : {project.stuname}'
      f'total: {project.calculate_total()} \n Average : {project.calculate_average()}')