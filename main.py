from flask import Flask, render_template
import requests

app = Flask(__name__)

qa_url = "https://api.npoint.io/b97c8cf96988a5eb4435"
response = requests.get(qa_url)
QA_ITEMS = response.json()


# Home Page
@app.route('/')
def home():
  return render_template('index.html')

# Guests Q&A
@app.route('/faq')
def blog_post():
  return render_template('faq.html', qa_items=QA_ITEMS)



if __name__ == "__main__":
  app.run(debug=True)