# -*- coding: utf-8 -*-
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def index():
	return "Hello World"

@app.route("/bababa/<name>/<name22>")
def aaa(name, name22):
	return """%s %s %s 
	Hello
	Goodbye
	""" %(name, name, name22)

@app.route("/file/")
def file_index():
	return """
	<html>
	  <body>
		<form action = "http://shimesaba.top:5000/file/upload" method = "POST" 
		     enctype = "multipart/form-data">
		        <input type = "file" name = "test_file" />
			    <input type = "submit"/>
	    </form>
      </body>
    </html>"""

@app.route("/file/upload", methods=['POST'])
def upload():
	f = request.files['test_file']
	f.save("./files/" + f.filename.encode('utf_8'))
	print type(f.filename)
	return "OK"

if __name__=="__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)

