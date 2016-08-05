'''
Created on Jul 10, 2016

@author: aadebuger
'''

from flask import Flask
from flask import request
app = Flask(__name__)

def logBatchitem(item):
	print(item)
def logBatch( batchv):
	map(lambda item:logBatchitem(item),batchv)
@app.route("/v1/batch",methods=['GET', 'POST'])
def hello():
    print("data=",request.json)

    batch = request.json['batch']
    logBatch(batch)
    return """{"status":"Hello World!"}"""

if __name__ == "__main__":
    app.run("0.0.0.0")
