from flask import Flask
import cx_Oracle as cx
import os

application = Flask(__name__)

@application.route("/")
def hello():
    print('about to connect')
    try:        
        cx.connect("oe/oracle@myserver1.test.com:1521/orc1")
        res = "Hello World"
    except cx_Oracle.DatabaseError as exc:
        print(str(type(exc)))                      # <class 'cx_Oracle.NotSupportedError'>
        print(repr(exc))                           # NotSupportedError('Variable_TypeByValue(): unhandled data type dict',)
        error = exc.args                          # "error" is a str, NOT a cx_Oracle._Error object
        print("Oracle-Error-Code:", str(error.code))   # AttributeError: 'str' object has no attribute 'code'
        print("Oracle-Error-Message:", str(error.message))
        res = str(error.message)
    return res

if __name__ == "__main__":
    application.run()
