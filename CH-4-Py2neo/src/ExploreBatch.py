'''
Created on 15-Mar-2015

@author: sagupta
'''
import py2neo
from py2neo import Graph, Node, Path, Rev
from py2neo.batch import *

class ExploreBatch(object):
    
    def __init__(self):
        '''
        Constructor
        '''
    def createAndExecuteBatchRequest(self):
        # Authenticate the user using py2neo.authentication
        # Ensure that you change the password 'sumit' as per your database configuration.
        py2neo.authenticate("localhost:7474", "neo4j", "sumit")
        # Connect to Graph and get the instance of Graph
        graph = Graph("http://localhost:7474/db/data/")
        
        #Get the instance of Write Batch request
        batch = WriteBatch(graph)
        #Create a Node
        daisy = Node(name='Daisy')
        # Now invoke create method on batch. It also shows another way of creating the Node
        batch.create({'name':'Hana'})
        batch.create(daisy)
        #Create a relationships between the Nodes
        batch.create((0,Rev('KNOWS'),1))
        #Finally submit the Nodes
        batch.submit()
        
if __name__ == '__main__':
    print("Start Batch request")
    #Create an Object of Class
    data = ExploreBatch()
    #Invoke the method to create and execute Batch request
    data.createAndExecuteBatchRequest()
    print("Finished Batch Request")
    
    