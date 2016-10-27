'''
Created on Jul 10, 2016

@author: aadebuger
'''

from flask import Flask
from flask import request
import json
app = Flask(__name__)
#curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X POST -d "{'batch':{'data':'here'}}" http://localhost:5000/v1/batch1

def logBatchitem(item):
	print(json.dumps(item,encoding='ascii'))
def logBatch( batchv):
	map(lambda item:logBatchitem(item),batchv)
@app.route("/")
def test():
    return """ok"""
@app.route("/v1/batch",methods=['GET', 'POST'])
def hello():
#    print("data1=",request)
    requestdata = request.get_json(force=True,silent=True)
#    print("data1=",requestdata)

    batch = requestdata['batch']
    logBatch(batch)
    return """{"status":"Hello World!"}"""

if __name__ == "__main__":
    app.run("0.0.0.0")
