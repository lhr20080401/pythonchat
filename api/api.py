from flask import Flask, render_template, request
import pymongo
#from pymongo import MongoClient 
app = Flask(__name__)

myclient = pymongo.MongoClient(host="mongodb+srv://cluster0.wc9bxyx.mongodb.net/myFirstDatabase",port="27017")
mydb = myclient["Cluster0"]
mydb.authenticate('admin','lhr368519')
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
