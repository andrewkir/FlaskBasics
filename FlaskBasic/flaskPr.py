from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = "Andrew"
    users = ["user1", 'user2', "test"]
    user_logged_in = True
    letters = list(name)
    info = {"name": name}
    return render_template("home.html", name=name, letters=letters, info=info, users=users,
                           user_logged_in=user_logged_in)


@app.route("/user/<name>")
def user_name(name):
    return render_template("user.html", name=name)


@app.route("/thank")
def thank():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('thank.html', first=first, last=last)


@app.route("/register")
def register():
    return render_template("signup.html")


@app.errorhandler(404)
def page_not_fount(e):
    return "nah, wrong one", 404


# start the development server using the run() method
if __name__ == "__main__":
    app.run(host='localhost', port=5000, threaded=True)
