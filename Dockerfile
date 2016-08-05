from python:2.7
run pip install flask
add src/main/python /code
workdir /code
cmd ["python","-m","shcloud.segmentrest"]
