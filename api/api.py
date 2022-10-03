from flask import Flask, render_template, request
import pymongo
#from pymongo import MongoClient 
app = Flask(__name__)


@app.route('/api/data/up_message/')
def up_message():
    myclient = pymongo.MongoClient("mongodb+srv://cluster0.hirzqvu.mongodb.net/myFirstDatabase:27017",username="haor",password="lhr368519")
    mydb = myclient["Cluster0"]
    mycol = mydb["sites"]
    lhr=1
    mydict = { "name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com" }
    global lhr
    mycol.insert_one(mydict) 
    return lhr
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
         f = request.files['file']
         
		
if __name__ == '__main__':
    app.run(debug = True)
