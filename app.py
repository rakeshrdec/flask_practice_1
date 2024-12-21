from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome"


@app.route('/success/<int:score>')
def score(score):
    return "The Person has success with Socre "+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has fail with Socre "+ str(score)

if __name__=='__main__':
    app.run(debug=True)