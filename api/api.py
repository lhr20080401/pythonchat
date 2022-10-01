from flask import Flask, render_template, request
import pymongo
app = Flask(__name__)
 
@app.route('/api/data/up_message/')
def upload_file():
     return "111"
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
         f = request.files['file']
         
		
if __name__ == '__main__':
    app.run(debug = True)