# -*- coding: utf-8 -*-
'''
Created on 2016年4月25日
 
@author: 55Haitao
'''
 
import threading
 
class Person(object):
    def __init__(self):
        print "init person"
         
    def speak(self):
        print "speak"
         
 
 
 
if __name__ == "__main__":
    p = Person()
    while True:
        timer = threading.Timer(5, Person.speak, (p,))
        print "start"
        timer.start()
        timer.join()
        print "after join"