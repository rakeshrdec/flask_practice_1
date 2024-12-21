from flask import Flask
### WSGI Application
app = Flask(__name__)


## Decorator WIth path
@app.route('/')
def welcome():
    return "Welcome to My FLask APP new changes after debug True"

@app.route('/members')
def members():
    return "Welcome to Members  new changes after debug True"


# @app.route('/')
# def welcome():
#     return "Welcome to My FLask APP new changes after debug True"


# @app.route('/')
# def welcome():
#     return "Welcome to My FLask APP new changes after debug True"



if __name__=='__main__':
    app.run(debug=True)