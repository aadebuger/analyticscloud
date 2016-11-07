'''
Created on Jul 10, 2016

@author: aadebuger
'''

from flask import Flask
from flask import request
import zlib
import json
import gzip
import StringIO
app = Flask(__name__)
#curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X POST -d "{'batch':{'data':'here'}}" http://localhost:5000/v1/batch1

def logBatchitem(item):
	print(json.dumps(item,encoding='ascii'))
def logBatch( batchv):
	map(lambda item:logBatchitem(item),batchv)
@app.route("/")
def test():
    return """ok"""
@app.route("/v1/projects/qkzhi/settings")
def settings():
    return """{  "integrations":     {
        "Segment.io": "@123"
    }  }"""
@app.route("/v1/batch",methods=['GET', 'POST'])
def hello():
    print("data1=",request)
    print("data1=",request.data)    
#	fp =gzip.Un(fileobj = StringIO.StringIO(request.data)
#	data = fp.read()
		
    udata = zlib.decompress(request.data, 15+32)
    
    print("udata=",udata)
    return """{"status":"Hello World!"}"""
    requestdata = request.get_json(force=True,silent=True)
#    print("data1=",requestdata)

    batch = requestdata['batch']
    logBatch(batch)
    return """{"status":"Hello World!"}"""

@app.route("/v1/import",methods=['GET', 'POST'])
def v1import():
    print("v1 import data1=",request)
    return """{"status":"Hello World!"}"""
   
if __name__ == "__main__":
    app.run("0.0.0.0")
