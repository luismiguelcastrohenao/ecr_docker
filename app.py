from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Vamos con toda</h1><br>' \
           '<h2>Have a Good day</h2>'
   
if __name__ == "__main__":
    app.run(debug=True)
