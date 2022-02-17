from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)

# to activate the virtual server please put in the terminal as follows (on windows PowerShell):
# Set-ExecutionPolicy -ExecutionPolicy unrestricted -Scope CurrentUser
# venv\Scripts\activate

# to run flask (on windows PowerShell) please put in the terminal as follows:
# set FLASK_APP=server.py
# $env:FLASK_APP = "server.py"
# flask run

# to make debugger mode ON please put in the terminal as follows:
# $env:FLASK_ENV = "development"

@app.route('/')
def my_start():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

# @app.route('/project.html')
# def my_project():
#     return render_template('project.html')
#
# @app.route('/contact.html')
# def my_contact():
#     return render_template('contact.html')

@app.route('/components.html')
def my_components():
    return render_template('components.html')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong, please try again'

# @app.route('/favicon.ico')
# def little_icon():
#     return "He was the chosen one... That is my thought"

# @app.route('/blog/2020/new')
# def newthought():
#     return "Now they say he wasn't, oh well."


