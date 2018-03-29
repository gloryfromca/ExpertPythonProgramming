import os
from flask import Flask
appexample = Flask(__name__)

@appexample.route('/name/<name>')
def root_(name):
    print("current process id:" + str(os.getpid()) + ": " + name)
    return name
