from flask import Flask
import cx_Oracle as cx
application = Flask(__name__)

@application.route("/")
def hello():
    res = cx.connect("oe/oracle@myserver1.test.com:1521/orc1")
    return "Hello World!", res

if __name__ == "__main__":
    application.run()
