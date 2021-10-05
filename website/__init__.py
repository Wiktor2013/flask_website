from flask import Flask, render_template, request, redirect, url_for, flash
import re

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

        def password_check(passwd):

            SpecialSym = ['$', '@', '#', '%']
            val = True

            if len(passwd) < 6:
                print('length should be at least 6')
                val = False

            if len(passwd) > 20:
                print('length should be not be greater than 8')
                val = False

            if not any(char.isdigit() for char in passwd):
                print('Password should have at least one numeral')
                val = False

            if not any(char.isupper() for char in passwd):
                print('Password should have at least one uppercase letter')
                val = False

            if not any(char.islower() for char in passwd):
                print('Password should have at least one lowercase letter')
                val = False

            if not any(char in SpecialSym for char in passwd):
                print('Password should have at least one of the symbols $@#')
                val = False
            if val:
                return val

        # Main method
        def main():
            passwd = 'Geek12@'

            if (password_check(passwd)):
                print("Password is valid")
            else:
                print("Invalid Password !!")

        # Driver Code
        if __name__ == '__main__':
            main()


        # if "@" not in email:
        #     flash("Podaj poprawny adres email", category="danger")
        # elif len(email) < 2:
        #     flash("Email za krotki", category="danger")
        # elif len(name) < 2:
        #     flash("Nazwa za krotka", category="danger")
        # elif len(password1) < 4:
        #     flash("Haslo powinno zawiera przynajmniej 4 znaki", category="danger")
        # elif password1 != password2:
        #     flash("Hasla nie sa takie same", category="danger")
        # else:
        #     flash( "Utworzono uzytkownika", category="success")
        #     return redirect(url_for('home'))

    return render_template("register.html", email=email, password1=password1, password2=password2, name=name)

@app.route("/login", methods=["GET", "POST"])
def login():
    def main():
        passwd = 'Geek12@'
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

        # compiling regex
        pat = re.compile(reg)

        # searching regex
        mat = re.search(pat, passwd)

        # validating conditions
        if mat:
            print("Password is valid.")
        else:
            print("Password invalid !!")
