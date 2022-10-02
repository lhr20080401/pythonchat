from flask import Flask, render_template, request
import pymongo
#from pymongo import MongoClient 
app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://cluster0.wc9bxyx.mongodb.net/myFirstDatabase:27017")
mongo_auth = myclient.admin
mongo_auth.authenticate('admin','lhr368519')
mydb = mongo_auth["Cluster0"]
mycol = mydb["sites"]

mydict = { "name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com" }
@app.route('/api/data/up_message/')
def up_message():
    mycol.insert_one(mydict) 
    return "true"
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
         f = request.files['file']
         
		
if __name__ == '__main__':
    app.run(debug = True)
