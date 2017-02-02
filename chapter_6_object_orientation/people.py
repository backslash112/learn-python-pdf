#!/usr/bin/env python

#
# This is a person class.
#

from datetime import datetime

class person(object):
    "Person Class"
    def __init__(self, name, age, parent = None):
        self.name = name
        self.age = age
        self.children = []
        print('Created', self.name, 'age', self.age)

    def setName(self, name):
        self.name = name
        print('Updated name', self.name)

    def setAge(self, age):
        self.age = age
        print('Updated age', self.age)

    def addChild(self, name, age):
        child = person(name, age, parent = self)
        self.children.append(child)
        print(self.name, ' added child ', child.name)

    def listChildren(self):
        if len(self.children) > 0:
            print(self.name, ' has children:')
            for c in self.children:
                print(' ', c.name)
        else:
            print(self.name, ' has no children.')

    def getChildren(self):
        return self.children
