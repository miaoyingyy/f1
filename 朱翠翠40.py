#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Student:
   '所有学生的基类'
   def __init__(self,primary,isLeagueNember):
      self.primary = primary
      self.isLeagueNember=isLeagueNember  
   if slef.primary=='primary'
      print'FLASE' 
   elif self.isLeagueNember=='isLeagueNember'
   print'TRUE'
   
   
class Student:        # 定义父类
   def canChemistry(self):
      print '调用父类方法'
 
class isLeagueNember: # 定义子类
   def canPhysics(self):
      print '调用子类方法'
 
c =isLeagueNember()          # 子类实例
c.canPhysics()         # 子类调用重写方法
