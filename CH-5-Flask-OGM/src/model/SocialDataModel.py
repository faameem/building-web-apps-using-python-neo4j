'''
Created on 16-Mar-2015

@author: sagupta
'''
class Person(object):

    def __init__(self, name=None,surname=None,age=None,country=None):
        self.name=name
        self.surname=surname
        self.age=age
        self.country=country

class Movie(object):
    
    def __init__(self, movieName=None):
        self.movieName=movieName
    
    