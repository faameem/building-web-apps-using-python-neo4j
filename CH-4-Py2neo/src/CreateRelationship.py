'''
Created on 13-Mar-2015

@author: sagupta
'''
import py2neo
from py2neo import Graph, Node, Relationship, Rev

def createRelationshipWithProperties():
    print("Start - Creating Relationships")
    # Authenticate the user using py2neo.authentication
    # Ensure that you change the password 'sumit' as per your database configuration.
    py2neo.authenticate("localhost:7474", "neo4j", "sumit")
    # Connect to Graph and get the instance of Graph
    graph = Graph("http://localhost:7474/db/data/")
    # Create Node with Properties
    amy = Node("FEMALE", name="Amy")
    # Create one more Node with Properties
    kristine = Node("FEMALE",name="Kristine")
    # Create one more Node with Properties
    sheryl = Node("FEMALE",name="Sheryl")
    
    #Define an Object of relationship which depicts the relationship between Amy and Kristine
    #We have also defined the properties of the relationship - "since=2005" 
    #By Default the direction of relationships is left to right, i.e. the -->
    kristine_amy = Relationship(kristine,"FRIEND",amy,since=2005)
    
    #This relationship is exactly same as the earlier one but here we are using "Rev"
    #"py2neo.Rev = It is used to define the reverse relationship (<--) between given nodes
    amy_sheryl=Relationship(amy,Rev("FRIEND"),sheryl,since=2001)
    
    #Finally use graph Object and Create Nodes and Relationship
    #When we create Relationship between, then Nodes are also created. 
    resultNodes = graph.create(kristine_amy,amy_sheryl)
    #Print the results (relationships)
    print("Relationship Created - ",resultNodes)


if __name__ == '__main__':
    createRelationshipWithProperties()
    