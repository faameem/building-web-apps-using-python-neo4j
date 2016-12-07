'''
Created on 18-Mar-2015

@author: sagupta
'''

from flask import Flask, request,jsonify
from flask_restful import Api, Resource 

webapp = Flask(__name__)
api = Api(webapp)

noOfVisitors = 0

@api.resource('/hello')
class HelloWorld(Resource):
    
    def get(self):
        return {'name':'Hello - this is GET'}
    
    def post(self):
        #Retrieve the JSON data from the Request and store it in local variable
        jsonData = request.get_json(cache=False)
        #Iterate over the JSON Data and print the data on console
        for key in jsonData:
            print(key,' = ',jsonData[key] )
        
        #reference to Global Variable
        global noOfVisitors
        #Adding 1 to the global Variable
        noOfVisitors = noOfVisitors + 1
        #Converting the response to JSON and returning back to user
        return jsonify(totalVisits = noOfVisitors)
    
    def put(self):
        return 'Hello world - this is PUT'
    
    def delete(self):
        return 'Hello  - this is DELETE'

if __name__ == '__main__':
    webapp. run(debug=True)