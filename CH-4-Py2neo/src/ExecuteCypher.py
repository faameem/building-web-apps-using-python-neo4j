'''
Created on 14-Mar-2015

@author: sagupta
'''

import py2neo
from py2neo import Graph

def connectGraph():
    # Authenticate the user using py2neo.authentication
    # Ensure that you change the password 'sumit' as per your database configuration.
    py2neo.authenticate("localhost:7474", "neo4j", "sumit")
    # Connect to Graph and get the instance of Graph
    graph = Graph("http://localhost:7474/db/data/")
    return graph

def executeSimpleCypherQuery():
    
    print("Start - execution of Simple Cypher Query")
    #Connect to Graph
    graph=connectGraph()
    #define and Execute a Cypher query which fetches all nodes from the database.
    #object of 'cypher' is returned by 'graph' Object and then further we use execute method Usully   
    results = graph.cypher.execute("MATCH (n) return n.name as name, labels(n) as labels")
    #Iterating ovver records and then printing the results.
    for index in range(len(results)):
        record = results[index]
        print("Printing Record = ",index," - Name = ",record.name,", Labels = ",record.labels)
          
    print("End - execution of Simple Cypher Query")

def executeStreamingCypherQuery():
    
    print("Start - execution of Streaming Cypher Query")
    #Connect to Graph
    graph=connectGraph()
    #Call to cyhper.stream method which returns cypher.RecordStream Object
    results = graph.cypher.stream("MATCH (n) return n.name as name, labels(n) as labels")
    #Iterating over the RecordStream Object and print the results
    for recordStream in results:
        print("Printing Record - Name = ",recordStream.name,", Labels = ",recordStream.labels)
          
    print("End - execution of Streaming Cypher Query")


def executeCypherQueryInTransaction():
    print("Start - execution of Cypher Query in Transaction")
    #Connect to Graph
    graph=connectGraph()
    #begin a transaction
    tx = graph.cypher.begin()
    #Add statements to the transaction
    tx.append("CREATE (n:Node1{name:'John'}) RETURN n")
    tx.append("CREATE (n:Node1{name:'Russell'}) RETURN n")
    tx.append("CREATE (n:Node1{name:'Smith'}) RETURN n")
    #Finally commit the transaction and get results
    results = tx.commit()
    #Iterate over results and print the results
    for result in results:
        for record in result:
            print(record.n)
    print("End - execution of Cypher Query in Transaction")
    
if __name__ == '__main__':
    executeSimpleCypherQuery()
    executeStreamingCypherQuery()
    executeCypherQueryInTransaction()
    