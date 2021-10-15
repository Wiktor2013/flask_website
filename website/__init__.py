from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dupa'


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        dane = dict(request.form)
        print(dane)
        #return f"Thanks, {request.form.get('name')}"
        with open("complaints.txt", "a") as f:
            f.write(dane["email"] + ";" + dane["email"] + ";" + dane["complain"] + "\n")
        return render_template("home.html", message=f"Thanks, {dane['name']}")

    return render_template("home.html", message="")


@app.route("/register", methods=["GET", "POST"])
def register():
    email = ""
    name = ""
    password1 = ""
    password2 = ""
    date = ""
    time = ""
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

    if "@" not in email:
        flash("Podaj poprawny adres email", category="danger")
    elif len(email) < 2:
        flash("Email za krotki", category="danger")
    elif len(name) < 2:
        flash("Nazwa za krotka", category="danger")
    elif len(password1) < 4:
        flash("Haslo powinno zawiera przynajmniej 4 znaki", category="danger")
    elif password1 != password2:
        flash("Hasla nie sa takie same", category="danger")
    else:
        flash( "Utworzono uzytkownika", category="success")
        return redirect(url_for('home'))

    return render_template("register.html", email=email, password1=password1, password2=password2, name=name)

