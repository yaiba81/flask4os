from flask import Flask
import cx_Oracle as cx
import sys
application = Flask(__name__)

@application.route("/")
def hello():
    try:
        if cx.connect("oe/oracle@myserver1.test.com:1521/orc1"):
            res = "Hello World"
    except:
        res = sys.exc_info()[0]
    return res

if __name__ == "__main__":
    application.run()
