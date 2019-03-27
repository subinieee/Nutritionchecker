from flask import Flask, render_template,request
import requests
from flask import jsonify

# def send_simple_message(userMail):
#    return requests.post(
#        "https://api.mailgun.net/v3/sandboxac414334ba8d4908849d76f3978027eb.mailgun.org/messages",
#        auth=("api", "9c52518eb0b6272713668b35a0c6d244-acb0b40c-a947cfdd"),
#        data={"from": "Excited User <mailgun@sandboxac414334ba8d4908849d76f3978027eb.mailgun.org>",
#              "to": [userMail],
#              "subject": "Hello",
#              "text": "Testing some Mailgun awesomness!"})

def checkrecipe(recipe):
    endpoint="https://api.nutritionix.com/v1_1/search"
    payload={"appId":"01f8af2c","appKey":"f9a14c81dcd43efdb4465a478369a4dd", "query":["recipe"]}
    response = requests.get(endpoint, params=payload)
    data=response.json()
    return data


app=Flask("MyApp")
@app.route("/<name>")
def hello():
    return "Hello World"
@app.route("/contact")
def hellosubin():
    return "Hello Subin"

@app.route("/")
def hellostranger():
    return render_template("h.html")


@app.route("/submit", methods=["POST"])
def sign_up():
    # if request.method == 'POST':
    data = request.form
    recipe_results = checkrecipe(data["recipe"])
    item = recipe_results["hits"][0]["fields"]["item_name"]
    return jsonify(item)

    # return render_template("submit.html")
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
