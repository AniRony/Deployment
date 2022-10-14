from flask import Flask

# initialize the APP

app = Flask(__name__ )
@app.route('/')
def home():
    return "Hello World"
# run the app
app.run()