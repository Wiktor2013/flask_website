from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        dane = dict(request.form)
        print(dane)
        #return f"Thanks, {request.form.get('name')}"
        with open("complaints.txt", "a") as f:
            f.write(dane["name"] + ";" + dane["email"] + ";" + dane["complain"] + "\n")
        return render_template("home.html", message=f"Thanks, {dane['name']}")

    return render_template("home.html", message="")

