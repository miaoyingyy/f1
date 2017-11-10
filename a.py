 #!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Student:
   '所有学生的基类'
   mail = 0
 
   def __init__(self,name,stu_no,stu_class,male):
      self.name = name
      self.stu_no = stu_no
      self.stu_class=stu_class
      self.male = male
      
   
   def displaystudent(self):
     print "Name : ", self.name, ",stu_no:",self.stu_class,"male:",self.male
 
