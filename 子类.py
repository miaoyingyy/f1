#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Student:
   '所有学生的基类'
   stu_count=0
   stu_count_male = 0
   stu_count_female= 0
   def __init__(self,stu_no,name,stu_class,male,female,stu_count):
      self.name = name
      self.stu_no = stu_no
      self.stu_class=stu_class
      self.male=male
      self.female=female
      Student.stu_count += 1   
   
   def displayStudent(self):
      print "Name : ", self.name,  ", stu_no ", self.stu_no,"stu_class:",self.stu_class,"male:",self.male
 
   def displayCount(self):
      print"Count: ",Student,stu_count
class Student:        # 定义父类
   def canChemistry(self):
      print '调用父类方法'
 
class isLeagueNember: # 定义子类
   def canPhysics(self):
      print '调用子类方法'
 
c =isLeagueNember()          # 子类实例
c.canPhysics()         # 子类调用重写方法
