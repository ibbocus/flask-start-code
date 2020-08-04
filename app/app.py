from flask import Flask, redirect, render_template, url_for, request
from datetime import date, datetime

# import flask

# In order for us to use flask, we need to create an instance of our app

app = Flask(__name__)


# Syntax to create flask instance


# Syntax for decorators to create a web route



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST': # To allow inputs from user to the page
        if request.form['username'] in open("data/user.txt", 'r').read() and request.form['password'] in open(f"{request.form['username']}pass.txt").read():
            # This reads to see if the username in the in the username file and if the password is correct. The password is stored in a unique file for each user
            return redirect(url_for('test'))
        elif len(open("data/attempts.txt", 'r').read()) > 2:
            file = open("data/attempts.txt", 'r+')
            file.truncate(0)
            file.close()
            return redirect(url_for('login_error'))
        elif request.form['username'] not in open("data/user.txt", 'r').read() or request.form['password'] not in open(f"{request.form['username']}pass.txt").read():
            with open('data/attempts.txt', 'a') as f:
                f.write("1")
    return render_template('index.html')

@app.route('/create_login', methods = ['GET', 'POST'])
def create_login():
    if request.method == 'POST':
        with open('data/user.txt', 'a') as f:
            username = request.form['userinput']
            f.write(username + "\n")
        with open(f'{username}pass.txt', 'a') as f:
            password = request.form['passinput']
            f.write(password + "\n")
    return render_template('create_login.html')

@app.route('/loginerror')
def login_error():
    return render_template('login_error.html')


@app.route('/home', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        with open('templates/answers.html', 'w') as f:
            f.write("Test started at: " + str(datetime.now()))
        score = 0
        if request.form['q1'] != "'#'":
            with open('templates/answers.html', 'a') as f:
                f.write("<br></br>" + "Q1: Wrong answer, the correct answer is: '#'")

        else:
            if request.form['q1'] == "#":
                with open('templates/answers.html', 'a') as f:
                    f.write("<br></br>" + "Q1: '#' is the correct answer")
                    score += 1

        if request.form['q2'] != "==":
            with open('templates/answers.html', 'a') as f:
                f.write("<br></br>" + "Q2: " + request.form['q2'] + " is the wrong answer, the correct answer is: ==")

        else:
            if request.form['q2'] == "==":
                with open('templates/answers.html', 'a') as f:
                    score += 1
                    f.write("<br></br>" + "Q2: == is the correct answer")
        with open('templates/answers.html', 'a') as f:
            f.write("<br></br>" + f"You have completed the test, your score is: {score}")
        return redirect(url_for('answers'))

    return render_template('testq.html')


@app.route('/answers')
def answers():
    return render_template('answers.html')


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
