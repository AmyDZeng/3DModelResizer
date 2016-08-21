import os
from flask import Flask, request, send_from_directory, make_response
from flask_cors import CORS, cross_origin
import time

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
	root_dir = os.path.dirname(os.path.realpath(__file__))
	filename = 'model' + '_' + str(int(time.time())) + '.obj'
	filepath = os.path.join(root_dir, 'generated', filename)

	os.system('blender -b models/sword/sword.blend --python script.py -- ' + filepath)

	response = make_response('http://10.71.134.218:5000/generated/' + filename)
	return response

@app.route("/generated/<path:filename>")
def download_file(filename):
	root_dir = os.path.dirname(os.path.realpath(__file__))
	print (os.path.join(root_dir, 'generated'))
	return send_from_directory(os.path.join(root_dir, 'generated'), filename, as_attachment=True)

if __name__ == "__main__":
	app.run(host='0.0.0.0')
