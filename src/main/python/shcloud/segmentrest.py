'''
Created on Jul 10, 2016

@author: aadebuger
'''

from flask import Flask
from flask import request
import json
app = Flask(__name__)

def logBatchitem(item):
	print(json.dumps(item,encoding='ascii'))
def logBatch( batchv):
	map(lambda item:logBatchitem(item),batchv)
@app.route("/v1/batch",methods=['GET', 'POST'])
def hello():
	requestdata = request.get_json(force=True)
    print("data=",requestdata)

    batch = requestdata['batch']
    logBatch(batch)
    return """{"status":"Hello World!"}"""

if __name__ == "__main__":
    app.run("0.0.0.0")
