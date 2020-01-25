from flask import Flask
import cx_Oracle as cx
import os

os.system("source /opt/app-root/etc/generate_container_user && \
    export LD_LIBRARY_PATH=/opt/app-root/src/instantclient_19_5:$LD_LIBRARY_PATH")

application = Flask(__name__)

@application.route("/")
def hello():
    try:
        print('will connect')
        cx.connect("oe/oracle@myserver1.test.com:1521/orc1")
        res = "Hello World"
    except cx_Oracle.DatabaseError as exc:
        print(str(type(exc)))                      # <class 'cx_Oracle.NotSupportedError'>
        print(repr(exc))                           # NotSupportedError('Variable_TypeByValue(): unhandled data type dict',)
        error, = exc.args                          # "error" is a str, NOT a cx_Oracle._Error object
        print("Oracle-Error-Code:", error.code)    # AttributeError: 'str' object has no attribute 'code'
        print("Oracle-Error-Message:", error.message)
        res = str(error.message)
    return res

if __name__ == "__main__":
    application.run()
