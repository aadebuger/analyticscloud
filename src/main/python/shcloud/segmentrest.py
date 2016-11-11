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
import json
app = Flask(__name__)
#curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X POST -d "{'batch':{'data':'here'}}" http://localhost:5000/v1/batch1



class WSGICopyBody(object):
    def __init__(self, application):
        self.application = application

    def __call__(self, environ, start_response):
        from cStringIO import StringIO
        input = environ.get('wsgi.input')
        length = environ.get('CONTENT_LENGTH', '0')
        length = 0 if length == '' else int(length)
        body = ''
        if length == 0:
            environ['body_copy'] = ''
            if input is None:
                return
            if environ.get('HTTP_TRANSFER_ENCODING','0') == 'chunked':
            	print("chunked")
                size = int(input.readline(),16)
#                print("size=",size)
                while size > 0:
                    body += input.read(size)
                    input.read(2)
                    size = int(input.readline(),16)
#                    print("size1=",size)
        else:
            body = environ['wsgi.input'].read(length)
        environ['body_copy'] = body
        environ['wsgi.input'] = StringIO(body)

        # Call the wrapped application
        app_iter = self.application(environ, 
                                    self._sr_callback(start_response))

        # Return modified response
        return app_iter

    def _sr_callback(self, start_response):
        def callback(status, headers, exc_info=None):

            # Call upstream start_response
            start_response(status, headers, exc_info)
        return callback
app.wsgi_app = WSGICopyBody(app.wsgi_app)

def logBatchitem(item):
	print(json.dumps(item,encoding='ascii'))
def logBatch( batchv):
	map(lambda item:logBatchitem(item),batchv)
@app.route("/")
def test():
    return """ok"""
   
@app.route("/v1/projects/qkzhiandroid/settings")
def androidsettings():
    return """{
    "integrations": {
        "Segment.io": {
            "apiKey": "qkzhiandroid"
        }
    },
    "plan": {
        "track": {
            "123": {
                "enabled": false,
                "integrations": {}
            },
            "Pixel Rendered": {
                "enabled": true,
                "integrations": {
                    "Amazon S3": false
                }
            },
            "Android: First Event Properties Event": {
                "enabled": true,
                "integrations": {
                    "Mixpanel": false
                }
            }
        }
    }
}"""
       

@app.route("/v1/projects/qkzhi/settings")
def settings():
    return """{  "integrations":     {
        "Segment.io": "@123"
    }  }"""
@app.route("/v1/batch",methods=['GET', 'POST'])
def hello():
#    print("data1=",request)
#    print("data1=",request.data)    
#	fp =gzip.Un(fileobj = StringIO.StringIO(request.data)
#	data = fp.read()

#    print("request.data datalen",len(request.data))
		
    data = request.get_data()
#    print("datalen",len(data))
    udata = zlib.decompress(data, 15+32)
    
#    print("udata=",udata)
#    return """{"status":"Hello World!"}"""
#    requestdata = request.get_json(force=True,silent=True)
#    print("data1=",requestdata)
    requestdata = json.loads(udata)
    batch = requestdata['batch']
    logBatch(batch)
    return """{"status":"Hello World!"}"""

@app.route("/v1/import",methods=['GET', 'POST'])
def importnew():
#    print("data1=",request)
#    print("data1=",request.data)    
#	fp =gzip.Un(fileobj = StringIO.StringIO(request.data)
#	data = fp.read()

#    print("request.data datalen",len(request.data))
		
#    data = request.data
    data=request.environ['body_copy']
#    print("datalen import",len(data))
    udata = zlib.decompress(data, 15+32)
    
#    print("udata=",udata)
#    return """{"status":"Hello World!"}"""
#    requestdata = request.get_json(force=True,silent=True)
#    print("data1=",requestdata)
    try:
    	requestdata = json.loads(udata)
     	batch = requestdata['batch']
      	logBatch(batch)
    	return """{"status":"Hello World!"}"""
    except Exception,e:
    	print(e)
    	return """{"status":"Hello World!"}"""    
@app.route("/v1/importold",methods=['GET', 'POST'])
def v1import():
    print("v1 import data1=",request)
    return """{"status":"Hello World!"}"""
   
if __name__ == "__main__":
    app.run("0.0.0.0")
