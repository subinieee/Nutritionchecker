from flask import Flask, render_template,request
import requests

def send_simple_message(userMail):
   return requests.post(
       "https://api.mailgun.net/v3/sandboxac414334ba8d4908849d76f3978027eb.mailgun.org/messages",
       auth=("api", "9c52518eb0b6272713668b35a0c6d244-acb0b40c-a947cfdd"),
       data={"from": "Excited User <mailgun@sandboxac414334ba8d4908849d76f3978027eb.mailgun.org>",
             "to": [userMail],
             "subject": "Hello",
             "text": "Testing some Mailgun awesomness!"})

app=Flask("MyApp")
@app.route("/")
def hello():
    return "Hello World"
@app.route("/subin")
def hellosubin():
    return "Hello Subin"

@app.route("/<name>")
def hellostranger(name):
    return render_template("h.html", name=name.title())


@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    print(form_data["email"])
    send_simple_message(form_data["email"])
    return "ALL OK"
#
# def send_simple_message():
#    return requests.post(
#        "https://api.mailgun.net/v3/sandboxac414334ba8d4908849d76f3978027eb.mailgun.org/messages",
#        auth=("api", "9c52518eb0b6272713668b35a0c6d244-acb0b40c-a947cfdd"),
#        data={"from": "Excited User <mailgun@sandboxac414334ba8d4908849d76f3978027eb.mailgun.org>",
#              "to": email,
#              "subject": "Hello",
#              "text": "Testing some Mailgun awesomness!"})



if __name__ == '__main__':

    app.run(debug=True)
