'''
Created on 16-Mar-2015

@author: sagupta
'''
from flask import Flask, redirect
from flask.helpers import url_for
from flask.templating import render_template

webapp = Flask(__name__)

@webapp.route("/")
def hello():
    return " Hello World!"

@webapp.route("/static", methods=['GET'])
def showStaticFiles():
    
    return redirect(url_for('static',filename='staticHTMLFile.html'))

@webapp.route("/showDynamic/<name>")
def renderDynamicContent(name=None):
    return render_template('dynamicTemplate.html',name=name)


if __name__ == '__main__':
    webapp.run(host='0.0.0.0',port=8999,debug=True)