from flask import Flask, render_template,request
import requests
from flask import jsonify


def checkrecipe(recipe):
    endpoint="https://api.edamam.com/api/food-database/parser"
    payload={"app_id":"1dbb4707","app_key":"e4c61d76694126307807831e256ba0cf", "ingr":recipe}
    response = requests.get(endpoint, params=payload)
    data=response.json()
    return data


app=Flask("MyApp")


@app.route("/")
def hellostranger():
    return render_template("h.html")


@app.route("/submit", methods=["POST"])
def sign_up():
    # if request.method == 'POST':
    data = request.form
    recipe_results = checkrecipe(data["recipe"])
    item = recipe_results['hints'][0]['food']['label']
    itemtwo = recipe_results['hints'][0]['food']['nutrients']
    return render_template("submit.html", myItem= item, myItemtwo=(itemtwo))

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
