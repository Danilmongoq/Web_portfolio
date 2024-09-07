from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
# debug mode: flask --app my_server --debug run
@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('contact_info.csv', mode='a') as contact_database:
        name = data["name"]
        email = data["email"]
        message = data["message"]

        fieldnames = ['Name', 'E-mail', 'Message']
        writer = csv.DictWriter(contact_database, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'Name': name, 'E-mail': email, 'Message': message})


@app.route("/submit_form", methods = ['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            # print(data)
            return redirect('thankyou.html')
        except:
            return 'Something went wronggg'
    else: 
        return 'Something went wrong with request.method'
    
