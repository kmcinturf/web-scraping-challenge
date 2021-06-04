from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import hemisphere_image_urls
import news_title
import news_p

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/marsdb")
  
@app.route("/")
def home():

      destination_data = mongo.db.collection.find_one()
      return render_template("index.html", mars=destination_data)

@app.route("/scrape")
def scrape():
     hemisphere_image_urls = Scrape.Scrape()

     mongo.db.collection.update({}, hemisphere_image_urls, upsert=True)

     return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
  
