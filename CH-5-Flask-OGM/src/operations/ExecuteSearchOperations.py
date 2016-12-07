'''
Created on 17-Mar-2015

@author: sagupta
'''
from py2neo import Graph
from py2neo.ext.ogm import Store
import py2neo

from model.SocialDataModel import Movie, Person

class SearchPerson(object):
    '''
    Class for Searching and retrieving the the People Node from server
    '''

    def __init__(self,host,port,username,password):
        py2neo.authenticate(host+':'+port, username, password)
        graph = Graph('http://'+host+':'+port+'/db/data/')
        store = Store(graph)
        self.graph=graph
        self.store=store
        
    def searchPerson(self,personName):
        cls = self.store.load_indexed('personIndex', 'name', personName, Person)
        
        return cls;
    

class SearchMovie(object):
    '''
    Class for Searching and retrieving the the Movie Node from server
    '''

    def __init__(self,host,port,username,password):
        py2neo.authenticate(host+':'+port, username, password)
        graph = Graph('http://'+host+':'+port+'/db/data/')
        store = Store(graph)
        self.graph=graph
        self.store=store
                
    def searchMovie(self,movieName):
        cls = self.store.load_indexed('movieIndex', 'name', movieName, Movie)
        
        return cls;