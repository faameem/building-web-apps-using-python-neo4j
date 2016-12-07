'''
Created on 16-Mar-2015

@author: sagupta
'''
from py2neo import Graph
from py2neo.ext.ogm import Store
import py2neo

from model.SocialDataModel import Movie, Person

class DeleteNodesRelationships(object):
    '''
    Define the Delete Operation on Nodes
    '''

    def __init__(self,host,port,username,password):
        #Authenticate and Connect to the Neo4j Graph Database
        py2neo.authenticate(host+':'+port, username, password)
        graph = Graph('http://'+host+':'+port+'/db/data/')
        store = Store(graph)
        #Store the reference of Graph and Store.
        self.graph=graph
        self.store=store
        
    def deletePersonNode(self,node):
        #Load the node from the Neo4j Legacy Index
        cls = self.store.load_indexed('personIndex', 'name', node.name, Person)
        #Invoke delete method of store class
        self.store.delete(cls[0])
        
    def deleteMovieNode(self,node):
        #Load the node from the Neo4j Legacy Index
        cls = self.store.load_indexed('movieIndex', 'name',node.movieName, Movie)
        #Invoke delete method of store class
        self.store.delete(cls[0])
        
    
class UpdateNodesRelationships(object):
    '''
     Define the Update Operation on Nodes
    '''

    def __init__(self,host,port,username,password):
        #Authenticate and Connect to the Neo4j Graph Database
        py2neo.authenticate(host+':'+port, username, password)
        graph = Graph('http://'+host+':'+port+'/db/data/')
        store = Store(graph)
        #Store the reference of Graph and Store.
        self.graph=graph
        self.store=store  
        
    def updatePersonNode(self,oldNode,newNode):
        #Get the old node from the Index
        cls = self.store.load_indexed('personIndex', 'name', oldNode.name, Person)
        #Copy the new values to the Old Node
        cls[0].name=newNode.name
        cls[0].surname=newNode.surname
        cls[0].age=newNode.age
        cls[0].country=newNode.country
        #Delete the Old Node form Index
        self.store.delete(cls[0])
        #Persist the updated values again in the Index
        self.store.save_unique('personIndex', 'name', newNode.name, cls[0])
    
    def updateMovieNode(self,oldNode,newNode):
        #Get the old node from the Index
        cls = self.store.load_indexed('movieIndex', 'name', oldNode.movieName, Movie)
        #Copy the new values to the Old Node
        cls[0].movieName=newNode.movieName
        #Delete the Old Node form Index
        self.store.delete(cls[0])
        #Persist the updated values again in the Index
        self.store.save_unique('personIndex', 'name', newNode.name, cls[0])
        
class CreateNodesRelationships(object):
    '''
    Define the Create Operation on Nodes
    '''

    def __init__(self,host,port,username,password):
        #Authenticate and Connect to the Neo4j Graph Database
        py2neo.authenticate(host+':'+port, username, password)
        graph = Graph('http://'+host+':'+port+'/db/data/')
        store = Store(graph)
        #Store the reference of Graph and Store.
        self.graph=graph
        self.store=store
        
    '''
    Create a person and store it in the Person Dictionary. 
    Node is not saved unless save() method is invoked. Helpful in bulk creation
    '''    
    def createPerson(self,name,surName=None,age=None,country=None):
        person = Person(name,surName,age,country)
        return person
    
    '''
    Create a movie and store it in the Movie Dictionary. 
    Node is not saved unless save() method is invoked. Helpful in bulk creation
    '''            
    def createMovie(self,movieName):
        movie = Movie(movieName)
        return movie
    
    '''
    Create a relationships between 2 nodes and invoke a local method of Store class. 
    Relationship is not saved unless Node is saved or save() method is invoked. 
    '''   
    def createFriendRelationship(self,startPerson,endPerson):
        self.store.relate(startPerson, 'FRIEND', endPerson)
    
    '''
    Create a TEACHES relationships between 2 nodes and invoke a local method of Store class. 
    Relationship is not saved unless Node is saved or save() method is invoked. 
    '''    
    def createTeachesRelationship(self,startPerson,endPerson):
        self.store.relate(startPerson, 'TEACHES', endPerson)
    '''
    Create a HAS_RATED relationships between 2 nodes and invoke a local method of Store class. 
    Relationship is not saved unless Node is saved or save() method is invoked. 
    '''    
    def createHasRatedRelationship(self,startPerson,movie,ratings):
        self.store.relate(startPerson, 'HAS_RATED', movie,{'ratings':ratings})
    '''
    Based on type of Entity Save it into the Server/ database
    '''
    def save(self,entity,node):
        if(entity=='person'):
            self.store.save_unique('personIndex', 'name', node.name, node)
        else:
            self.store.save_unique('movieIndex','name',node.movieName,node)
            

    
        
        

