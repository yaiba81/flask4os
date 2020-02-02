from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():    
    return "Hello"

if __name__ == "__main__":
    application.run()
