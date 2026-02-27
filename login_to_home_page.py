from flask import (
    Flask, render_template, url_for,
    request, redirect
)

app = Flask(__name__)

password:str = "alezandro"
username:str = "alezandro"


# login page
# note to self
# when you launch the website with 'localhost:5000'. You want to add '/login' since that is the route for this 
@app.route("/login")
def login_page():
    return render_template('login.html')

@app.route("/hello_world", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        if (request.form["user_name_data"] == username) and (request.form["user_password_data"] == password):
            return render_template("home_page.html")
        
        else:
            return "Wrong password"
    
    else:
        # will 'redirect' to another app.route method
        return redirect("/")
    

@app.route("/")
def main_home_page():
    return render_template('home_page.html')


@app.route("/create_account")
def create_account():
    return render_template("create_account.html")
    


if __name__ == "__main__":
    app.run(debug=True)
