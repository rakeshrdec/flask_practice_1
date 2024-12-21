from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('marks_form.html')

@app.route('/success/<int:score>')
def success(score):
    # return "The Person has success with Socre "+ str(score)
    return render_template('result.html',score=score)

@app.route('/fail/<int:score>')
def fail(score):
    # return "The Person has fail with Socre "+ str(score)
    return render_template('result.html',score=score)


@app.route('/submit-marks', methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        n1 = float(request.form['student1_marks'])
        n2 = float(request.form['student2_marks'])
        n3 = float(request.form['student3_marks'])
        total_score = n1+n2+n3
        avg = float(total_score)/3
        print(avg)
        if avg > 50:
            return redirect(url_for('success',score=int(total_score)))
        else:
            return redirect(url_for('fail',score=int(total_score)))

if __name__=='__main__':
    app.run(debug=True)